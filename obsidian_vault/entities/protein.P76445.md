---
entity_id: "protein.P76445"
entity_type: "protein"
name: "lpxT"
source_database: "UniProt"
source_id: "P76445"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17660416}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:17660416}. Note=Transferase activity takes place on the periplamic side of the inner membrane. {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:18047581}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxT yeiU b2174 JW2162"
---

# lpxT

`protein.P76445`

## Static

- Type: `protein`
- Source: `UniProt:P76445`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17660416}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:17660416}. Note=Transferase activity takes place on the periplamic side of the inner membrane. {ECO:0000255|HAMAP-Rule:MF_01945, ECO:0000269|PubMed:18047581}.

## Enriched Summary

FUNCTION: Involved in the modification of the lipid A domain of lipopolysaccharides (LPS). Transfers a phosphate group from undecaprenyl pyrophosphate (C55-PP) to lipid A to form lipid A 1-diphosphate. Contributes to the recycling of undecaprenyl phosphate (C55-P) (PubMed:18047581). In vitro, has low undecaprenyl-diphosphate phosphatase activity (PubMed:17660416). {ECO:0000269|PubMed:17660416, ECO:0000269|PubMed:18047581}. LpxT transfers a phosphate group from undecaprenyl-pyrophosphate (Und-PP or C55-PP) to the position 1 phosphate of approximately one-third of lipid A-core oligosaccharide molecules to create lipid A-core 1-diphosphate. LpxT activity enhances the net negative charge of LPS and contributes to recycling of the carrier lipid CPD-9646 that is required for biosynthesis of a number of cell wall polymers such as peptidoglycan and lipopolysaccharide. LpxT activity contributes to DEOXYCHOLATE resistance; lpxT inactivation impairs the initial stages of gut colonization in a mouse model of infection; inhibition of LpxT by the small membrane protein MONOMER0-4214 PmrR results in sensitivity to deoxycholate in the polymyxin-resistant EG11615 BasR(PmrA)-constitutive strain WD101 (see also ). In trans expression of lpxT in WD101 restores deoxycholate resistance and confers polymyxin B susceptibility . LpxT is a membrane protein with its C-terminus in the cytoplasm...

## Biological Role

Catalyzes RXN-16281 (reaction.ecocyc.RXN-16281), RXN0-5383 (reaction.ecocyc.RXN0-5383), UNDECAPRENYL-DIPHOSPHATASE-RXN (reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Involved in the modification of the lipid A domain of lipopolysaccharides (LPS). Transfers a phosphate group from undecaprenyl pyrophosphate (C55-PP) to lipid A to form lipid A 1-diphosphate. Contributes to the recycling of undecaprenyl phosphate (C55-P) (PubMed:18047581). In vitro, has low undecaprenyl-diphosphate phosphatase activity (PubMed:17660416). {ECO:0000269|PubMed:17660416, ECO:0000269|PubMed:18047581}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16281|reaction.ecocyc.RXN-16281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5383|reaction.ecocyc.RXN0-5383]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN|reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2174|gene.b2174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76445`
- `KEGG:ecj:JW2162;eco:b2174;ecoc:C3026_12165;`
- `GeneID:75172303;946693;`
- `GO:GO:0005886; GO:0009103; GO:0009245; GO:0016776; GO:0043165; GO:0050380; GO:1903412`
- `EC:2.7.4.29`

## Notes

Lipid A 1-diphosphate synthase (EC 2.7.4.29) (Kdo(2)-lipid A phosphotransferase) (Undecaprenyl pyrophosphate:lipid A 1-phosphate phosphotransferase)
