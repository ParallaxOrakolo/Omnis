import Vue from 'vue';
import Router from 'vue-router';

import Dashboard from '@/views/Dashboard.vue';
import Devices from '@/views/settings/Devices.vue';
import Home from '@/views/Home.vue';
import IntroLogo from '@/views/IntroLogo.vue';
import Network from '@/views/settings/Network.vue';
import NodeConfig from '@/views/NodeConfig.vue';
import NodeEditor from '@/components/node/NodeEditor.vue';
import NodeWorkspace from '@/views/NodeWorkspace.vue';
import Progress from '@/views/Progress.vue';
import Scan from '@/views/Scan.vue';
import Settings from '@/views/Settings.vue';
import Success from '@/views/Success.vue';
import System from '@/views/settings/System.vue';
import Support from '@/views/settings/Support.vue';
import Process from '@/views/settings/Process.vue';
import Users from '@/views/settings/Users.vue';
import Personalize from '@/views/settings/Personalize.vue';
import RegisterUser from '@/views/Auth/RegisterUser.vue';
import ProcessObjects from '@/views/settings/ProcessObjects.vue';
import ProcessMyProcess from '@/views/settings/ProcessMyProcess.vue';
import ProcessVariables from '@/views/settings/ProcessVariables.vue';
import ProcessMatrix from '@/views/settings/ProcessMatrix.vue';
import ObjectEditor from '@/components/settings/process/ObjectEditor.vue';
import VariableRegister from '@/components/settings/process/VariableRegister.vue';
import MatrixEditor from '@/components/settings/process/MatrixEditor.vue';
import VariableEdit from '@/components/settings/process/VariableEdit.vue';
import ProcessEditor from '@/components/settings/process/ProcessEditor.vue';

Vue.use(Router);

const routes = [
  {
    name: 'home',
    path: '/home',
    component: Home,
  },
  {
    name: 'settings',
    path: '/config',
    redirect: '/config/system',
    component: Settings,
    meta: {
      breadCrumb: 'settings.name',
    },
    children: [
      {
        name: 'system',
        component: System,
        path: 'system',
        meta: {
          breadCrumb: 'settings.system.name',
        },
      },
      {
        name: 'network',
        component: Network,
        path: 'network',
        meta: {
          breadCrumb: 'settings.networkAndInternet.name',
        },
      },
      {
        name: 'devices',
        component: Devices,
        path: 'devices',
        meta: {
          breadCrumb: 'settings.devices.name',
        },
      },
      {
        name: 'users',
        component: Users,
        path: 'users',
        meta: {
          breadCrumb: 'settings.users.name',
        },
        children: [
          {
            name: 'registerUser',
            component: RegisterUser,
            path: ':register-user',
            meta: { breadCrumb: 'settings.users.registerUser.name' },
          },
        ],
      },
      {
        name: 'personalize',
        component: Personalize,
        path: 'settings.personalize.name',
      },
      {
        name: 'support',
        component: Support,
        path: 'support',
        meta: {
          breadCrumb: 'settings.support.name',
        },
      },
      {
        name: 'process',
        component: Process,
        path: 'process',
        meta: {
          breadCrumb: 'settings.process.name',
        },
        children: [
          {
            name: 'myProcess',
            component: ProcessMyProcess,
            path: 'myProcess',
            meta: { breadCrumb: 'settings.process.process.name' },
            children: [
              {
                name: 'processRegister',
                component: ProcessEditor,
                path: 'add',
                props: true,
                meta: { breadCrumb: 'settings.process.process.add' },
              },
              {
                name: 'processEdit',
                component: ProcessEditor,
                path: 'edit',
                props: true,
                meta: { breadCrumb: 'settings.process.process.edit' },
              },
            ],
          },
          {
            name: 'matrix',
            component: ProcessMatrix,
            path: 'matrix',
            meta: { breadCrumb: 'settings.process.matrix.name' },
            children: [
              {
                name: 'matrixRegister',
                component: MatrixEditor,
                path: 'add',
                props: true,
                meta: { breadCrumb: 'settings.process.matrix.add' },
              },
              {
                name: 'matrixEdit',
                component: MatrixEditor,
                path: 'edit',
                props: true,
                meta: { breadCrumb: 'settings.process.matrix.edit' },
              },
            ],
          },
          {
            name: 'object',
            component: ProcessObjects,
            path: 'object',
            meta: { breadCrumb: 'settings.process.objects.name' },
            children: [
              {
                name: 'objectEditor',
                component: ObjectEditor,
                path: 'add',
                meta: { breadCrumb: 'settings.process.objects.add' },
              },
              {
                name: 'objectEdit',
                component: ObjectEditor,
                path: 'edit',
                props: true,
                meta: { breadCrumb: 'settings.process.objects.edit' },
              },
            ],
          },
          {
            name: 'variable',
            component: ProcessVariables,
            path: 'variable',
            meta: { breadCrumb: 'settings.process.variables.name' },
            children: [
              {
                name: 'variableRegister',
                component: VariableRegister,
                path: 'add',
                meta: { breadCrumb: 'settings.process.variables.add' },
              },
              {
                name: 'variableEdit',
                component: VariableEdit,
                path: 'edit',
                props: true,
                meta: { breadCrumb: 'settings.process.variable.edit' },
              },
            ],
          },
        ],
      },
      // {
      //   name: 'matrix',
      //   component: MatrixDirectionSelector,
      //   path: ':matrix',
      //   meta: {
      //     breadCrumb: 'Matriz', //crumb
      //   },
      // },
    ],
  },
  {
    name: 'intro-logo',
    path: '/',
    component: IntroLogo,
  },
  {
    name: 'scan',
    path: '/scan',
    component: Scan,
  },
  {
    name: 'progress',
    path: '/progress',
    component: Progress,
  },
  {
    name: 'success',
    path: '/success',
    component: Success,
  },
  {
    name: 'dashboard',
    path: '/dashboard',
    component: Dashboard,
  },
  {
    name: 'node',
    path: '/node',
    component: NodeWorkspace,
  },
  {
    name: 'nodeEditor',
    path: '/node-editor',
    component: NodeEditor,
  },
  {
    name: 'nodeConfig',
    path: '/node-config',
    component: NodeConfig,
  },
  // {
  //   path: '*',
  //   redirect: '/',
  // },
];

const router = new Router({ ...{ mode: 'history' }, routes });

// router.beforeEach((to, from) => {
//   // ...
//   // explicitly return false to cancel the navigation
//   return false
// })

export default router;
