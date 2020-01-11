from qgis._core import QgsTask, QgsProject
from .mqttSubscriber import mqttSubscriber

class guiUpdater(QgsTask):
    subscriber = mqttSubscriber()

    def __init__(self):
        QgsTask.__init__(self)

    def run(self):
        return True

    def finished(self, result):
        if not guiUpdater.subscriber.isEmpty():
             # Retrieve heatmap
             layer = QgsProject.instance().mapLayersByName('radiation_heatmap copy_energy_plant')[0]
             radiations = guiUpdater.subscriber.getRadiationList()
             layer.startEditing()
             index = 0
             it = layer.getFeatures()
             for feat in it:
                 layer.changeAttributeValue(feat.id(), 5, radiations[index])
                 index = index + 1
             layer.commitChanges()

    def cancel(self):
        super().cancel()
