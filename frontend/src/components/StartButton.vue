<template>
  <div>
    <!-- <v-img src="http://192.168.1.30:5000" height="250" class="text-right pa-2"> -->
    </v-img>
    <v-btn rounded x-large @click="startProcess()" color="warning" dark>
      <span
        ><v-icon left>{{ icon ? icon : 'mdi-play' }}</v-icon></span
      >
      {{ text ? text : 'iniciar' }}
    </v-btn>

    <v-row justify="center">
      <v-dialog v-model="dialog" :max-width="step1 ? '600' : '450'">
        <v-card>
          <v-card-title class="text-h5 pt-6 pb-8" v-if="step1"
            >Escolha o modelo da peça!</v-card-title
          >
          <v-card-title class="text-h5 pt-6 pb-8" v-else
            ><v-btn class="mr-2" text icon small @click="step1 = true"
              ><v-icon>mdi-arrow-left</v-icon></v-btn
            >
            Quantas peças deseja produzir?</v-card-title
          >
          <v-item-group v-if="step1">
            <v-container>
              <v-row class="d-flex flex-row align-center justify-space-around">
                <div v-for="(item, i) in ListOfPartsToMount" :key="i">
                  <v-item v-slot="{ active, toggle }">
                    <div class="partItem pa-5">
                      <v-card
                        :elevation="active ? '3' : '0'"
                        @click="
                          toggle,
                            (step1 = false),
                            (selectedPart = item.partNumber)
                        "
                        class="rounded-circle"
                      >
                        <v-img
                          :src="require(`@/assets/img/${item.src}`)"
                          height="250"
                          class="text-right pa-2"
                        >
                        </v-img>
                      </v-card>
                      <v-card-title class="text-h6 d-flex justify-center mt-n4"
                        >{{ item.partName }}
                        v-row
                        <span class="font-weight-regular"
                          >|{{ item.partNumber }}</span
                        >
                      </v-card-title>
                    </div>
                  </v-item>
                </div>
              </v-row>
            </v-container>
          </v-item-group>

          <v-card-text
            class="flex-column d-flex justify-center mt-6"
            v-if="!step1"
          >
            <v-btn-toggle
              v-model="selection"
              color="warning"
              class="d-flex justify-center"
            >
              <v-btn
                value=""
                v-on:click="
                  () => {
                    SEND_MESSAGE({
                      command: actions.START_PROCESS,
                      parameter: {
                        total: 99999,
                        onlyCorrectParts: state.operation.onlyCorrectParts
                          ? state.operation.onlyCorrectParts
                          : false,
                        partId: selectedPart,
                      },
                    });
                    //startStatusChage
                    dialog = false;
                    state.operation.total = 0;
                    state.operation.finished = false;
                    toPage('progress');
                  }
                "
              >
                <span>ilimitadas</span>
              </v-btn>
              <v-btn>
                <span>quantidade especifica</span>
              </v-btn>
            </v-btn-toggle>

            <!-- <v-btn class="mx-2 mb-4" large> ilimitada </v-btn>
            <v-btn class="mx-2" large> quantidade especifica </v-btn> -->

            <v-row
              class="mt-6 ml-n7 d-flex justify-center mb-4"
              v-if="selection == 1"
            >
              <div>
                <v-row class="d-flex align-baseline mb-6">
                  <v-btn
                    class="mx-2"
                    fab
                    small
                    @click="less()"
                    :disabled="buttomDisable"
                  >
                    <v-icon dark> mdi-minus </v-icon>
                  </v-btn>

                  <v-text-field
                    filled
                    dense
                    rounded
                    v-model="state.operation.total"
                    class="mt-0 pt-0 quantityToProduce"
                    hide-details
                    single-line
                    type="number"
                    min="1"
                  ></v-text-field>

                  <v-btn
                    class="mx-2"
                    fab
                    small
                    @click="state.operation.total++, (buttomDisable = false)"
                  >
                    <v-icon dark> mdi-plus </v-icon>
                  </v-btn>
                  <v-btn
                    class="ml-6"
                    color="warning"
                    rounded
                    v-on:click="
                      () => {
                        SEND_MESSAGE({
                          command: actions.START_PROCESS,
                          parameter: {
                            total: state.operation.total,
                            onlyCorrectParts: state.operation.onlyCorrectParts
                              ? state.operation.onlyCorrectParts
                              : false,
                            partId: selectedPart,
                          }, // Change selection -> state.operation.total -HB
                        });
                        //startStatusChage
                        dialog = false;
                        state.operation.finished = false;
                        toPage('progress');
                      }
                    "
                  >
                    iniciar
                  </v-btn>
                </v-row>

                <v-row class="ml-n16 d-flex justify-center" v-if="selection">
                  <v-checkbox
                    v-model="state.operation.onlyCorrectParts"
                    label="Considerar apenas peças corretas"
                    color="orange"
                    hide-details
                  ></v-checkbox>
                </v-row>
              </div>
            </v-row>

            <!-- <v-divider></v-divider> -->
          </v-card-text>

          <!-- <v-card-actions class="d-flex justify-center">
              <v-btn color=" darken-1" text @click="dialog = false">
                Cancelar
              </v-btn>
              
          </v-card-actions> -->
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
import { actions } from '../store/index';
import gql from 'graphql-tag';

export default {
  // mixins: [mixins],
  name: 'StartButton',

  props: {
    text: String,
    icon: String,
  },

  data: () => ({
    selectedPart: 1,
    // onlyCorrectParts: true,
    selection: false,
    actions,
    dialog: false,
    buttonDisable: false,
    step1: true,
    ListOfPartsToMount: [
      {
        partNumber: 0,
        partName: 'Menor',
        src: 'estribo-quadrado.png',
      },
      {
        partNumber: 1,
        partName: 'Maior',
        src: 'estribo-retangular.png',
      },
    ],
  }),

  components: {},

  apollo: {},

  computed: {
    ...mapGetters(['state']),
    ...mapActions(['socket_userMessage']),
  },

  methods: {
    ...mapMutations(['SEND_MESSAGE', 'NEW_MESSAGE']),

    async startProcess() {
      this.dialog = true;
      console.log('startProcess');
      const response = await this.$apollo.query({
        query: gql`
          query {
            getProcess {
              data {
                status
              }
            }
          }
        `,
      });
      console.log(this.$apollo.store);
      this.lixo = response.data.getProcess.data.status;
    },

    toPage(page) {
      if (this.$route.name != page) {
        this.$router.push('/' + page);
      }
    },

    less() {
      if (this.state.operation.total >= 2) {
        this.state.operation.total--;
      } else {
        this.buttomDisable = true;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.quantityToProduce {
  width: 100px;
}

.partItem {
  height: 320px;
  width: 250px;
}
.v-card--link:focus:before {
  opacity: 0;
}
</style>
