<template>
  <!-- <div class=" align-center"> -->
  <div class="d-flex align-center breadcrumb">
    <v-btn
      icon
      large
      class="mr-n4 ml-n10"
      @click="$router.back()"
      alt
      v-if="crumbs.length !== 1"
    >
      <v-icon>mdi-chevron-left</v-icon>
    </v-btn>
    <!-- <div class="text-h4">{{ $route.name }}</div> -->
    <v-breadcrumbs :items="crumbs">
      <template v-slot:item="{ item }" class="text">
        <v-breadcrumbs-item>
          <router-link :to="makePath(item)">
            <span
              :class="
                $t($router.currentRoute.meta.breadCrumb) == item.text
                  ? 'text-h4 text--primary'
                  : 'text-h6 text--grey'
              "
              >{{ item.text }}</span
            >
          </router-link>
        </v-breadcrumbs-item>
      </template>
      <template v-slot:divider>
        <v-icon>mdi-chevron-right</v-icon>
      </template>
    </v-breadcrumbs>
    <div></div>
  </div>
</template>

<script>
import { menuList } from '@/components/settings/menuDescription';

export default {
  data() {
    return {
      items: menuList,
      // items: [
      //   {
      //     text: 'Configurações',
      //     href: 'config/system',
      //     disabled: false,
      //   },
      //   {
      //     text: 'Assembly',
      //     href: 'config/network',
      //     disabled: false,
      //   },
      // ],
    };
  },
  computed: {
    crumbs() {
      const pathArray = this.$route.path.split('/');
      pathArray.shift();
      // console.log('path', pathArray);
      const breadcrumbs = pathArray.reduce((breadcrumbArray, path, idx) => {
        breadcrumbArray.push({
          path,
          to: breadcrumbArray[idx - 1]
            ? `/${breadcrumbArray[idx - 1].path}/${path}`
            : `/${path}`,
          text: this.$t(this.$route.matched[idx].meta.breadCrumb) || path,
        });
        // console.log('fasdfasdfa', breadcrumbArray);
        return breadcrumbArray.filter((a) => a.path !== 'config');
      }, []);
      // console.log('breadcrumbs', breadcrumbs);
      return breadcrumbs;
    },
  },
  methods: {
    makePath(item) {
      const finalIndex = this.crumbs.findIndex((object) => object.path === item.path);

      let path = '/';
      // console.log(this.crumbs.map((el) => el.to));
      const newPath = this.crumbs
        .map((el) => el.to)
        .reduce((previousValue, currentValue, index) => {
          path = previousValue;
          if (index <= finalIndex) {
            path = previousValue + currentValue;
          }
          return path;
        });
      // console.log('path', newPath);
      return `/config${newPath}`;
    },
  },
};
</script>
<style lang="scss" scoped>
.breadcrumb {
  margin-left: -24px;
}
::v-deep .v-breadcrumbs {
  padding-top: 13px;
}
</style>
