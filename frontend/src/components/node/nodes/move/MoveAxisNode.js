import { Node } from '@baklavajs/core';
// import { store } from '../../main';

export default class MoveAxisNode extends Node {
  type = 'MoveAxisNode';
  twoColumn = true;

  height = 800;

  name = 'Mover Eixo';

  axisList = [
    { name: 'X', isActive: false, value: 0, homing: false },
    { name: 'Y', isActive: false, value: 0, homing: false },
    { name: 'Z', isActive: false, value: 0, homing: false },
    { name: 'A', isActive: false, value: 0, homing: false },
    { name: 'B', isActive: false, value: 0, homing: false },
    { name: 'C', isActive: false, value: 0, homing: false },
    { name: 'F', isActive: false, value: 0, homing: false },
  ];

  board = { name: '', id: '' };

  constructor() {
    super();
    // const axisList = ["X", "Y", "Z"];
    // this.addInputInterface('X');
    // this.addInputInterface('Y');
    // this.addInputInterface('Z');
    this.addInputInterface('Gatilho', undefined, undefined, {
      description:
        'Entrada que fará o acionamento do nó',
    });
    this.addInputInterface('XY', undefined, undefined, {
      description:
        'Recebe uma lista de coordenadas para executar o movimento',
    });
    this.addOutputInterface('Sucesso');
    this.addOutputInterface('Falha');
    this.axisList.forEach((axis) => {
      // if (axis.isActive) {
      if (axis.name === 'F') {
        this.addInputInterface('Velocidade');
      } else {
        this.addInputInterface(axis.name);
        // }
      }
    });
   

    // this.axisList.forEach((axis) => {
    //   this.addOption(axis[0], 'CheckboxOption');
    // });

    // this.events.update.addListener(this, (event) => {
    // });

    // this.events.update.addListener(this, (event) => {
    //   // console.log(this.interfaces.entries());
    //   console.log('axis');
    //   const item = this.axisList.find((axis) => axis == event.name);
    //   console.log(item);
    //   console.log(event.name);
    //   if (event.name === item) {
    //     if (this.getOptionValue(item)) {
    //       this.addInputInterface(`${item} `);
    //     } else {
    //       this.removeInterface(`${item} `);
    //     }
    //   }
    // });

    this.addOption('axisList', 'MoveAxisDialog', this.axisList);
    this.addOption('board', undefined, this.board);
    this.addOption('color', undefined, '#FF9800');
    this.addOption('running', undefined, true);
  }
}
