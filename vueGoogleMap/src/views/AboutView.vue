
    <template>
  <GoogleMap
    api-key="AIzaSyDBpSqjBzXiRgpQthUa5Fng62OI_z2sHMM"
    :libraries="['visualization']"
    style="width: 100%; height: 500px"
    :center="sanFrancisco"
    :zoom="13"
  >
    <HeatmapLayer :options="{ data: heatmapData }" />
  </GoogleMap>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, HeatmapLayer } from "vue3-google-map";

export default defineComponent({
  components: { GoogleMap, HeatmapLayer },
  setup() {
    const sanFrancisco = { lat: 37.774546, lng: -122.433523 }

    const heatmapData = [
      { location: { lat: 37.782, lng: -122.447 }, weight: 0.5 },
      { lat: 37.782, lng: -122.445 },
      { location: { lat: 37.782, lng: -122.443 }, weight: 2 },
      { location: { lat: 37.782, lng: -122.441 }, weight: 3 },
      { location: { lat: 37.782, lng: -122.439 }, weight: 2 },
      { lat: 37.782, lng: -122.437 },
      { location: { lat: 37.782, lng: -122.435 }, weight: 0.5 },

      { location: { lat: 37.785, lng: -122.447 }, weight: 3 },
      { location: { lat: 37.785, lng: -122.445 }, weight: 2 },
      { lat: 37.785, lng: -122.443 },
      { location: { lat: 37.785, lng: -122.441 }, weight: 0.5 },
      { lat: 37.785, lng: -122.439 },
      { location: { lat: 37.785, lng: -122.437 }, weight: 2 },
      { location: { lat: 37.785, lng: -122.435 }, weight: 3 },
    ];

    return {
      sanFrancisco,
      heatmapData,
    }
  },
});
</script>