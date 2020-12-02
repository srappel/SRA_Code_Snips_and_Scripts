Private Sub btCopy_Click(sender As Object, e As EventArgs) Handles btCopy.Click
        Dim pOID As Integer = My.Settings.CurrentOID
        If My.Settings.CurrentOID = 0 Then
            MsgBox("Please load a feature to copy by entering an OID or loading a selected feature.")
            Exit Sub
        
        End If

        'Try
        '    'Fills the form with the records form the original, with the exception of spatial fields and shape.
        '    FillForm(pOID)
        'Catch ex As Exception
        '    MsgBox("There was an error when filling the form:" & vbCrLf & ex.ToString())
        '    Exit Sub
        'End Try

        'This part will actually edit the shape and the x and y fields
        Dim pFeatureLayer As IFeatureLayer = GDXTools.getInstance.GetGeodexLayer
        Dim pFeatureClass As IFeatureClass = pFeatureLayer.FeatureClass
        Dim pFeature As IFeature = pFeatureClass.GetFeature(pOID)
        Dim pShape As IGeometry = pFeature.Shape
        Dim pDataset As IDataset = pFeatureClass
        Dim pWorkspace As IWorkspace = pDataset.Workspace
        Dim pWorkspaceEdit As IWorkspaceEdit = pWorkspace
        Dim pRecord As Record = New Record
        pRecord.X1 = pFeature.Value(pFeature.Fields.FindField("X1"))
        pRecord.X2 = pFeature.Value(pFeature.Fields.FindField("X2"))
        pRecord.Y1 = pFeature.Value(pFeature.Fields.FindField("Y1"))
        pRecord.Y2 = pFeature.Value(pFeature.Fields.FindField("Y2"))

        Try
            pWorkspaceEdit.StartEditing(True)
            pWorkspaceEdit.StartEditOperation()

            Dim pNewFeature As IFeature = pFeatureClass.CreateFeature()
            pNewFeature.Shape = pShape
            pNewFeature.Value(pFeature.Fields.FindField("X1")) = pRecord.X1
            pNewFeature.Value(pFeature.Fields.FindField("X2")) = pRecord.X2
            pNewFeature.Value(pFeature.Fields.FindField("Y1")) = pRecord.Y1
            pNewFeature.Value(pFeature.Fields.FindField("Y2")) = pRecord.Y2

            pNewFeature.Store()
            pWorkspaceEdit.StopEditOperation()
            pWorkspaceEdit.StopEditing(True)

            If pNewFeature.HasOID = True Then
                Dim pNewOID As Integer = pNewFeature.OID
                lblOID.Text = pNewOID.ToString()
                lblMSG1.Text = "The feature with OID " & pOID.ToString() & " has been copied and a new feature with OID " & pNewOID.ToString() &
                    " has been created."
               
                My.Settings.CurrentOID = pNewFeature.OID

            Else
                MsgBox("WARNING: The new feature has no Object ID!", MsgBoxStyle.OkOnly)
                lblOID.Text = "..."
                My.Settings.CurrentOID = pOID
                Exit Sub
            End If

        Catch ex As Exception
            MsgBox("There was an error copying the shape of the feature." & vbCrLf & ex.ToString, MsgBoxStyle.OkOnly)
            lblOID.Text = "..."
            Exit Sub
        End Try
    End Sub