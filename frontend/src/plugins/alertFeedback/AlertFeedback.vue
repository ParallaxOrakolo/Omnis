<template>
  <div class="warper">
    <div @mouseover="mouseUp = true" @mouseleave="mouseUp = false, mouseLeave()">
      <div v-for="(alert, i) in alertList" :key="i">
        <v-snackbar
          v-on="timer(alert.description)"
          :style="{ 'padding-bottom': calcMargin(i) }"
          v-model="snackbar"
          rounded="pill"
          :color="alert.type"
          :timeout="99999"
          transition="fade-transition"
        >
          <!-- {{(alertList.length - (i+1))*3000}} -->
          {{ alert.description }}
          <v-tooltip top v-if="alert.moreInfo">
            <template v-slot:activator="{ on, attrs }">
              <v-icon class="ml-1" dark v-bind="attrs" v-on="on" small
                >mdi-information-outline</v-icon
              >
            </template>
            <span>{{ alert.moreInfo }}</span>
          </v-tooltip>
          <template v-slot:action="{ attrs }">
            <v-btn small icon v-bind="attrs" @click="closeDialog()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </template>
        </v-snackbar>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'AlertFeedback',
  data() {
    return {
      defaultTimeout: 8000,
      snackbar: true,
      mouseUp: false,
    };
  },

  computed: mapState('alert', {
    alertList: (state) => state.alertList,
  }),

  created() {},

  methods: {
    ...mapActions('alert', ['removeItemList']),
    calcMargin(i) {
      const margin = i * 60 + 'px';
      return margin;
    },

    closeDialog() {
      this.removeItemList();
      // this.alertList.pop();
    },

    mouseLeave() {
      setTimeout(() => {
        if (!this.mouseUp) {
          this.alertList.pop();
        }
        // console.log('this.alertList');
      }, 2000);
    },

    timer(description) {
      setTimeout(() => {
        if (!this.mouseUp) {
          this.alertList.pop();
        }
        // console.log('this.alertList');
      }, this.calculateTimeout(description));
    },

    calculateTimeout(description) {
      // console.log('_________________________________________');
      // console.log(description);
      const words = description.split(' ').length;
      // console.log('words', words);
      const timeout = words * 600;
      // console.log('timeout', timeout);
      if (timeout < this.defaultTimeout) {
        // console.log('timeout defalut', this.defaultTimeout);
        return this.defaultTimeout;
      }
      return timeout;
    },
  },
};
</script>

<style lang="scss" scoped>
.warper {
  z-index: 99999999;
}
</style>
