import { Node } from '@baklavajs/core';
// import { store } from '../../main';

export default class MoveAxis extends Node {
  type = 'move-axis';
  twoColumn = true;

  height = 800;

  name = 'Mover Eixo';

  axisList = [
    { name: 'X', isActive: true, value: 0 },
    { name: 'Y', isActive: true, value: 0 },
    { name: 'Z', isActive: true, value: 0 },
    { name: 'F', isActive: true, value: 0 },
  ];

  board = 'default';

  constructor() {
    super();
    // const axisList = ["X", "Y", "Z"];
    // this.addInputInterface('X');
    // this.addInputInterface('Y');
    // this.addInputInterface('Z');
    this.addInputInterface('Trigger');
    this.addOutputInterface('onSuccess');
    this.addOutputInterface('onFailure');
    this.axisList.forEach((axis) => {
      if (axis.isActive) {
        if (axis.name === 'F') {
          this.addInputInterface('Velocidade');
        } else {
          this.addInputInterface(axis.name);
        }
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
    this.addOption('board', 'MoveAxisDialog', this.board);
    this.addOption('color', undefined, '#FF9800');
    this.addOption('running', undefined, true);
  }
}
