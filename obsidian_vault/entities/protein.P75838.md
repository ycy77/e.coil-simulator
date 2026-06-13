---
entity_id: "protein.P75838"
entity_type: "protein"
name: "ycaO"
source_database: "UniProt"
source_id: "P75838"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycaO b0905 JW0888"
---

# ycaO

`protein.P75838`

## Static

- Type: `protein`
- Source: `UniProt:P75838`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in beta-methylthiolation of ribosomal protein S12. {ECO:0000269|PubMed:21169565}. The YcaO protein is involved in the β-methylthiolation of EG10911-MONOMER. YcaO interacts directly with a ribonucleoprotein complex containing S12 . The molecular function of E. coli YcaO is unknown; however, the YcaO domain and its ATP binding motif define the YcaO superfamily which includes proteins that catalyze cyclodehydration, amidation and thioamidation reactions . Crystal structures of apo- and nucleotide-bound YcaO have been solved, showing a circularly symmetric homodimer. The protein consists of an N-terminal domain with a broadly conserved and previously unknown ATP-binding fold and a C-terminal dimerization domain. The purified protein hydrolyzes ATP to AMP and pyrophosphate in vitro . A ycaO deletion mutant contains significantly reduced levels of β-methylthiolated ribosomal protein S12 and has an altered transcriptional profile similar to that of a rimO deletion mutant . Review:

## Biological Role

Catalyzes ATP-PYROPHOSPHATASE-RXN (reaction.ecocyc.ATP-PYROPHOSPHATASE-RXN).

## Annotation

FUNCTION: Involved in beta-methylthiolation of ribosomal protein S12. {ECO:0000269|PubMed:21169565}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ATP-PYROPHOSPHATASE-RXN|reaction.ecocyc.ATP-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0905|gene.b0905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75838`
- `KEGG:ecj:JW0888;eco:b0905;ecoc:C3026_05585;`
- `GeneID:93776513;945509;`
- `GO:GO:0000287; GO:0005829; GO:0047693`

## Notes

Ribosomal protein S12 methylthiotransferase accessory factor YcaO
