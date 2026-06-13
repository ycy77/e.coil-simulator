---
entity_id: "protein.P0ABG4"
entity_type: "protein"
name: "ftsW"
source_database: "UniProt"
source_id: "P0ABG4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00913, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:12423747, ECO:0000269|PubMed:9603865}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00913, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:12423747, ECO:0000269|PubMed:9603865}. Note=Localizes to the division septum. Localization requires FtsZ, FtsA, FtsQ and FtsL, but not FtsI."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsW b0089 JW0087"
---

# ftsW

`protein.P0ABG4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABG4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00913, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:12423747, ECO:0000269|PubMed:9603865}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00913, ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:12423747, ECO:0000269|PubMed:9603865}. Note=Localizes to the division septum. Localization requires FtsZ, FtsA, FtsQ and FtsL, but not FtsI.

## Enriched Summary

FUNCTION: Peptidoglycan polymerase that is essential for cell division (Probable). Functions probably in conjunction with the penicillin-binding protein 3 (ftsI) (PubMed:11807049, PubMed:9603865). Required for localization of FtsI (PubMed:11807049). {ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:9603865, ECO:0000305|PubMed:27643381, ECO:0000305|PubMed:9218774}. The SEDS family protein FtsW is is believed to be the primary peptidoglycan (PG) glycosyltransferase which functions together with its cognate transpeptidase EG10341-MONOMER "FtsI" (PBP3) to synthesize septal peptidoglycan (sPG) during cell division; FtsW-FtsI are the SEDS-bPBP pair of the divisome. The spatiotemporal coordination of sPG synthesis in E. coli is currently described by a 'two-track' model (see ). FtsW is an essential cell division protein that is conserved in most walled bacteria; the protein is produced at low levels and localizes to the septum . FtsW is an integral membrane protein belonging to the SEDS (shape, elongation, division, sporulation) family; it is predicted to consist of 10 transmembrane (TM) segments with both the N- and C-terminal end located in the cytoplasm . Subcomplexes of SEDS proteins with class 2 penicillin binding proteins are proposed to be the primary peptidoglycan synthases in cell elongation and division...

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179), RXN-16650 (reaction.ecocyc.RXN-16650).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

FUNCTION: Peptidoglycan polymerase that is essential for cell division (Probable). Functions probably in conjunction with the penicillin-binding protein 3 (ftsI) (PubMed:11807049, PubMed:9603865). Required for localization of FtsI (PubMed:11807049). {ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:9603865, ECO:0000305|PubMed:27643381, ECO:0000305|PubMed:9218774}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0089|gene.b0089]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABG4`
- `KEGG:ecj:JW0087;eco:b0089;ecoc:C3026_00350;`
- `GeneID:93777345;946322;`
- `GO:GO:0000917; GO:0005886; GO:0008360; GO:0008955; GO:0009252; GO:0015648; GO:0032153; GO:0043093; GO:0051301; GO:0071555; GO:1990586`
- `EC:2.4.99.28`

## Notes

Probable peptidoglycan glycosyltransferase FtsW (PGT) (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) (Lipid II flippase FtsW) (Peptidoglycan polymerase) (PG polymerase)
