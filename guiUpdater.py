import qgis
from qgis._core import QgsTask, QgsProject, QgsHeatmapRenderer, QgsStyle
from qgis.PyQt.QtGui import QColor
from .mqttSubscriber import mqttSubscriber
import math
class guiUpdater(QgsTask):
    subscriber = mqttSubscriber()
    MAX_AREA = 96116.84105212608
    MAX_RADIATION_VALUE = 200
    initilRadius = MAX_RADIATION_VALUE / (4 * math.pi)

    def __init__(self):
        QgsTask.__init__(self)

    def run(self):
        return True

    def finished(self, result):
        layer = QgsProject.instance().mapLayersByName('radiation_heatmap copy_energy_plant')[0]
        if not guiUpdater.subscriber.isEmpty():
             # Retrieve heatmap
             radiations = guiUpdater.subscriber.getRadiationList()
             layer.startEditing()
             index = 0
             it = layer.getFeatures()
             for feat in it:
                 layer.changeAttributeValue(feat.id(), 5, radiations[index])
                 index = index + 1
             layer.commitChanges()

        canvas = qgis.utils.iface.mapCanvas()
        print(canvas.extent().area())
        if 4000 <= canvas.extent().area() <= int(self.MAX_AREA):
            self.newScaledRender(1.2,layer)
        if 1000 <= canvas.extent().area() <= 4000:
            self.newScaledRender(1.4, layer)
        if 300 <= canvas.extent().area() <= 1000:
            self.newScaledRender(2.2, layer)
        if  80 <= canvas.extent().area() <= 300:
            self.newScaledRender(5, layer)
        if  0 <= canvas.extent().area() <= 80:
            self.newScaledRender(15, layer)
        #offset = self.MAX_AREA - canvas.extent().area()
        #print(canvas.extent().area())
        # renderer = QgsHeatmapRenderer()
        #
        # renderer.setRadius(self.initilRadius + offset)
        # style = QgsStyle.defaultStyle()
        # defaultColorRampNames = style.colorRampNames()
        #
        # ramp = style.colorRamp(defaultColorRampNames[8])
        # ramp.setColor1(QColor(0, 0, 4, 0))
        # renderer.setColorRamp(ramp)
        # layer.setRenderer(renderer)

    def cancel(self):
        super().cancel()

    def newScaledRender(self,newScale,layer):
        renderer = QgsHeatmapRenderer()

        renderer.setRadius(int(newScale * self.MAX_RADIATION_VALUE / (4 * math.pi)))
        renderer.setWeightExpression("Radiation")
        renderer.setRenderQuality(1)
        style = QgsStyle.defaultStyle()
        defaultColorRampNames = style.colorRampNames()

        ramp = style.colorRamp(defaultColorRampNames[8])
        ramp.setColor1(QColor(0, 0, 4, 0))
        renderer.setColorRamp(ramp)
        layer.setRenderer(renderer)