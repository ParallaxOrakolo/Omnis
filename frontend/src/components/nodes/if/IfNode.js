import { Node } from '@baklavajs/core';
// import { store } from '../../main';

export default class IfNode extends Node {
  type = 'IfNode';
  // twoColumn = true;

  name = 'Condicional IF';

  inputList = [{ name: 'A' }, { name: 'B' }, { name: 'C' }, { name: 'F' }];

  constructor() {
    super();

    this.inputList.forEach((input) => {
      this.addInputInterface(input.name);
    });

    this.addInputInterface('Expressão');

    this.addInputInterface('Verdadeiro', undefined, undefined, {
      description:
        "Se a condição inserida for falsa, ele passa o que recebeu aqui para a saida de 'Falha' ",
    });

    this.addInputInterface('Falso', undefined, undefined, {
      description:
        "Se a condição inserida for verdadeira, ele passa o que recebeu aqui para a saida de 'Sucesso' ",
    });
    // this.addInputInterface('Falso', undefined, 'Text3');

    this.addOutputInterface('Sucesso', {
      description: 'Se tudo der certo sai por aqui ',
    });

    this.addOutputInterface('Falha');

    this.addOption('expression', 'IfDialog', null);
    this.addOption('onFailure', undefined, null);
    this.addOption('onSuccess', undefined, null);
    this.addOption('inputList', undefined, this.inputList);

    this.addOption('color', undefined, '#ff3900');
    this.addOption('running', undefined, true);
  }
}
