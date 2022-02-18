export const descriptions = [
  // just use icons only from material design https://materialdesignicons.com/
  {
    name: 'Operações Matemáticas',
    type: 'math',
    text: `
            Com esse node você será capaz de fazer operações matemáticas
        `,
    icon: 'calculator-variant',
    examples: `Quando precisamos subtrair dar uma margem da lateral da maquina
    `,
    category: 'Utilidades',
    tags: ['json', 'mapping', 'object'],
  },
  {
    name: 'Blur (Borrar)',
    type: 'filter-blur',
    text: `
            Esse node é capaz de borrar uma imagem
        `,
    icon: 'blur',
    examples: `Esse filtro é util quando precisamos suavizar uma borda que é imperfeita 
    `,
    category: 'Filtros',
    tags: ['filter', 'blur', 'borrar', 'borrado', 'imagem', 'filtros'],
  },
  {
    name: 'Detecção de Borda',

    type: 'filter-canny',
    text: ` 
            Esse node é capaz de detectar bordas de uma imagem
        `,
    icon: 'border-all-variant',
    examples: `
            Esse filtro é util quando precisamos detectar bordas de uma imagem
        `,
    category: 'Filtros',
    tags: ['filter', 'canny', 'bordas', 'imagem', 'filtros'],
  },
  {
    name: 'Comunicação Serial',
    type: 'serial',
    text: `
            Esse node é capaz de enviar dados para um arduino
        `,
    icon: 'serial-port',
    examples: `
            Esse node é capaz de enviar dados para um arduino
        `,
    category: 'Hardware',
    tags: ['serial', 'arduino', 'comunicação', 'comunicacao'],
  },
  {
    name: 'Camera',
    type: 'camera',
    text: `
            Esse node é capaz de capturar uma imagem da camera
        `,
    icon: 'camera',
    examples: `
            Esse node é capaz de capturar uma imagem da camera
        `,
    category: 'Hardware',
    tags: ['camera', 'hardware', 'comunicacao', 'comunicacao'],
  },
  {
    name: 'Alerta',
    type: 'alert',
    text: ` 
           Esse node envia um alerta para o usuário
    `,
    icon: 'alert',
    examples: `
            Se precisar enviar um alerta para quando precisar de uma ajuda ou algo do tipo
        `,
    category: 'Feedback',
    tags: ['alert', 'utilidades', 'utilidade', 'feedback', 'depuração'],
  },
  {
    name: 'log',
    type: 'log',
    text: ` Esse armazena a informação toda vez que passa pelo node. 
    `,
    icon: 'console-line',
    examples: `
            Caso você queira ver o resultado de uma operação matemática toda vez que passe a informação por aquele node
        `,
    category: 'Feedback',
    tags: ['log', 'utilidades', 'utilidade', 'feedback', 'depuração'],
  },
];

export function getCategoryList() {
  return [...new Set(descriptions.map((description) => description.category))];
}

export function getDescription(nodeType) {
  const description = descriptions.find((descr) => descr.type === nodeType);

  if (description) return description.text;
  else return 'No description provided for node';
}

export function getTags(nodeType) {
  const description = descriptions.find((descr) => descr.type === nodeType);

  if (description) return description.tags;
  else return [];
}
