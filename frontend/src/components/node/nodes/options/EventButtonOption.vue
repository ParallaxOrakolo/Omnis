<template>
  <div class="opt-container">
    <v-btn
      :disabled="$store.getters.dataChanged"
      class="btn-execute"
      outlined
      @click="onClick"
      color="blue lighten-2"
      small
    >
      {{ option.title }}
    </v-btn>
    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-chip
          v-on="on"
          class="btn-counter ml-1 justify-center"
          outlined
          style="height: 28px"
          color="green lighten-2"
          label
          small
          @contextmenu.prevent="resetCounter"
          >{{ executionCount }}</v-chip
        >
      </template>
      <span>Number of executions</span>
    </v-tooltip>
  </div>
</template>

<script>
// import { apiBaseUrl, socketio } from '@/main.js';

export default {
  props: ['option', 'node', 'value'],
  data: () => ({
    executionCount: 0,
  }),

  created() {
    // socketio.on('EXEC_COUNT', (data) => {
    //   if (data.nodeId === this.node.id) {
    //     this.executionCount = data.triggerCount || 0;
    //   }
    // });
  },
  methods: {
    onClick() {
      // socketio.emit("BTN_CLICK", this.node.id);
    },
    resetCounter() {
      // let resetUrl = `${apiBaseUrl}/reset/${this.node.id}`;
      // this.axios.get(resetUrl).then(() => {
      //   console.log("%cSuccessfully resetted ", this.node.name);
      // });
    },
  },
};
</script>

<style scoped>
.opt-container {
  display: grid;
  grid-template-columns: 3fr 1fr;
  grid-template-rows: 1fr;
  padding: 0px;
}

.btn-execute {
  grid-column-start: 1;
  grid-column-end: 1;
  grid-row-start: 1;
  grid-row-end: 1;
  height: 90%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-counter {
  grid-column-start: 2;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 1;
}
</style>
