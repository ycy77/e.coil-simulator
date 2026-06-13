---
entity_id: "protein.P0AEI4"
entity_type: "protein"
name: "rimO"
source_database: "UniProt"
source_id: "P0AEI4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rimO yliG b0835 JW0819"
---

# rimO

`protein.P0AEI4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEI4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the methylthiolation of the residue Asp-89 of ribosomal protein uS12. {ECO:0000269|PubMed:18252828, ECO:0000269|PubMed:21169565}. RimO was identified as the methyltransferase responsible for methylthiolation of the β carbon of the D88 residue of EG10911-MONOMER . RimO belongs to the methylthiotransferase (MTTase) family of the superfamily of radical-SAM proteins and is the only MTTase known to catalyze methylthiolation of a protein substrate . RimO interacts directly with a ribonucleoprotein complex containing S12; it seems likely that the enzyme is only able to modify S12 efficiently in the context of the small ribosomal subunit . RimO contains two spectroscopically distinguishable [4Fe-4S] clusters . The reaction is thought to take place in two steps , however this has not been shown for RimO in E. coli. It is thought that the G7511 YgfZ protein is involved in the repair/exchange of the spent cluster of both RimO and the homologous enzyme G6364 MiaB. The in vivo activity of RimO is very low in the absence of YgfZ . A rimO mutant contains the unmodified form of S12 and grows more slowly than the wild-type strain . A rimO deletion mutant has an altered transcriptional profile similar to a ycaO deletion mutant, primarily affecting members of the Fnr and Nar regulons . RimO: "ribosomal modification" Reviews:

## Biological Role

Catalyzes RXN0-6366 (reaction.ecocyc.RXN0-6366). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Catalyzes the methylthiolation of the residue Asp-89 of ribosomal protein uS12. {ECO:0000269|PubMed:18252828, ECO:0000269|PubMed:21169565}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6366|reaction.ecocyc.RXN0-6366]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0835|gene.b0835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEI4`
- `KEGG:ecj:JW0819;eco:b0835;ecoc:C3026_05230;`
- `GeneID:75204700;945465;`
- `GO:GO:0005829; GO:0006400; GO:0035599; GO:0046872; GO:0051539; GO:0103039`
- `EC:2.8.4.4`

## Notes

Ribosomal protein uS12 methylthiotransferase RimO (uS12 MTTase) (uS12 methylthiotransferase) (EC 2.8.4.4) (Ribosomal protein uS12 (aspartate(89)-C(3))-methylthiotransferase) (Ribosome maturation factor RimO)
