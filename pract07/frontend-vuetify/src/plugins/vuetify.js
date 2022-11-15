import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            primary: colors.green.accent3,
            secondary: colors.deepOrange.lighten1
          },
          dark: {
            primary: '#90CAF9',
            secondary: '#E91E63'
          },
        },
      },
});
