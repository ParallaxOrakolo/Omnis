<template>
  <div>
    <h1>Sidebar Option</h1>
    <p>This is an advanced option</p>
    <p>{{ value.testtext }}</p>
    <input-option v-model="value.testtext"></input-option>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { InputOption } from "@baklavajs/plugin-options-vue";

@Component({
  components: { InputOption }
})
class SidebarOption extends Vue {
  @Prop()
  value!: any;
}

export default SidebarOption;
</script>
