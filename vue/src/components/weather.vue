<template>
    <div class="weather">
        <div id="he-plugin-standard"></div>
    </div>
</template>

<script>
    export default {
        name: 'weather',
        mounted() {
            let script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = 'https://widget.qweather.net/standard/static/js/he-standard-common.js?v=2.0';
            document.body.appendChild(script);

            this.containerHeight = document.documentElement.clientHeight;
            this.containerWidth = document.documentElement.clientWidth;
            window.addEventListener('resize', () => {
                this.containerHeight = document.documentElement.clientHeight;
                this.containerWidth = document.documentElement.clientWidth;
            });

            window.WIDGET = {
                "CONFIG": {
                    "layout": "1",
                    "width": this.containerWidth * 0.5,
                    "height": this.containerHeight * 0.5,
                    "background": "1",
                    "dataColor": "FFFFFF",
                    "borderRadius": "5",
                    "key": "631bc69f82f045e58950fd878a997346"
                }
            };
        }
    }
</script>

<style>
    .weather {
        position: relative;
        display: flex;
        margin-top: 9%;
        justify-content: center;
    }

    .weather img {
        transform: scale(1.2);
    }

    .weather .wv-lt-refresh {
        display: none;
    }
</style>