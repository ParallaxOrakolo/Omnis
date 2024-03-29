<template>
  <div :id="data.id" :class="classes">
    <div
      class="__port"
      @mouseover="startHover"
      @mouseout="endHover"
      :style="color"
    ></div>
    <v-tooltip
      :left="this.data.isInput"
      :right="!this.data.isInput"
      open-delay="400"
      max-width="200"
      transition="fade-transition"
      :disabled="!data.description"
    >
      <template v-slot:activator="{ on, attrs }">
        <span
          v-bind="attrs"
          v-on="on"
          v-if="
            data.connectionCount > 0 ||
            !data.option ||
            !getOptionComponent(data.option)
          "
          class="align-middle"
        >
          {{data.alias?data.alias:displayName }}
        </span>
      </template>
      <span>{{ displayDescription }}</span>
    </v-tooltip>
  </div>
</template>

<script>
import { socketio } from '@/main';

export default {
  data() {
    return {
      isActive: false,
      isConnected: false,
    };
  },
  inject: ['editor', 'plugin'],
  props: {
    data: Object,
    name: String,
    description: String,
    type: Object,
  },
  mounted() {
    this.plugin.hooks.renderInterface.execute(this);
  },
  updated() {
    this.plugin.hooks.renderInterface.execute(this);
  },
  beforeMount() {
    this.value = this.data.value;
    this.data.events.setValue.addListener(this, (v) => {
      this.value = v;
    });
    this.data.events.setConnectionCount.addListener(this, (c) => {
      this.$forceUpdate();
      this.isConnected = c > 0;
    });
    this.data.events.updated.addListener(this, () => {
      this.$forceUpdate();
    });
    this.isConnected = this.data.connectionCount > 0;
  },
  created() {
    // socketio.on('INTERFACE_STATE', (data) => {
    //   if (data.some(elem => elem === this.data.id)) {
    //     this.isActive = true;
    //   } else {
    //     this.isActive = false;
    //   }
    // });
  },
  methods: {
    startHover() {
      this.editor.hoveredOver(this.data);
    },
    endHover() {
      this.editor.hoveredOver(undefined);
    },
    getOptionComponent(name) {
      if (!name || !this.plugin.options) {
        return;
      }
      let options = this.plugin.options[name];
      return options;
    },
  },
  computed: {
    classes() {
      return {
        'node-interface': true,
        '--input': this.data.isInput,
        '--output': !this.data.isInput,
        '--connected': this.isConnected,
        labelActive: this.isActive,
      };
    },
    displayName() {
      return this.data.displayName || this.name;
    },
    displayDescription() {
      return this.data.description || this.description;
    },
    color() {
      if (this.data.type === 'JSON') return { 'background-color': 'orange' };
      if (this.data.type === 'XML') return { 'background-color': 'blue' };
      if (this.data.type === 'Message') return { 'background-color': 'blue' };
      return { 'background-color': 'white' };
    },
  },
  watch: {
    'data.type': {
      handler(newValue) {
        this.plugin.hooks.renderInterface.execute(this);
      },
      deep: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.labelActive {
  color: limegreen;
}

.v-tooltip ::v-deep {
  opacity: 1;
}
</style>
