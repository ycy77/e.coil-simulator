---
entity_id: "protein.P0AEJ4"
entity_type: "protein"
name: "envZ"
source_database: "UniProt"
source_id: "P0AEJ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1323560, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2824492}; Multi-pass membrane protein {ECO:0000305|PubMed:1323560, ECO:0000305|PubMed:15919996, ECO:0000305|PubMed:2824492}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "envZ ompB perA tpo b3404 JW3367"
---

# envZ

`protein.P0AEJ4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEJ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1323560, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2824492}; Multi-pass membrane protein {ECO:0000305|PubMed:1323560, ECO:0000305|PubMed:15919996, ECO:0000305|PubMed:2824492}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:2997120, PubMed:3536870). EnvZ functions as a membrane-associated protein kinase that phosphorylates OmpR in response to environmental signals; at low osmolarity OmpR activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113). Also dephosphorylates OmpR in the presence of ATP (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2668281). The cytoplasmic dimerization domain (CDD) forms an osmosensitive core; increasing osmolarity stabilizes this segment (possibly by its contraction), enhancing the autophosphorylation rate and consequently, downstream phosphotransfer to OmpR and signaling (PubMed:22543870, PubMed:28256224). Autophosphorylation is greater when full-length EnvZ is reconstituted in a lipid environment, lipid-mediated allostery impacts the kinase function of EnvZ (PubMed:28256224). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation, and suggests that EnvZ senses cytoplasmic acidic pH (PubMed:29138484)...

## Biological Role

Component of sensor histidine kinase EnvZ (complex.ecocyc.ENVZ-CPLX), EnvZ-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-ENVZ).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:2997120, PubMed:3536870). EnvZ functions as a membrane-associated protein kinase that phosphorylates OmpR in response to environmental signals; at low osmolarity OmpR activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113). Also dephosphorylates OmpR in the presence of ATP (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2668281). The cytoplasmic dimerization domain (CDD) forms an osmosensitive core; increasing osmolarity stabilizes this segment (possibly by its contraction), enhancing the autophosphorylation rate and consequently, downstream phosphotransfer to OmpR and signaling (PubMed:22543870, PubMed:28256224). Autophosphorylation is greater when full-length EnvZ is reconstituted in a lipid environment, lipid-mediated allostery impacts the kinase function of EnvZ (PubMed:28256224). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation, and suggests that EnvZ senses cytoplasmic acidic pH (PubMed:29138484). {ECO:0000269|PubMed:1323560, ECO:0000269|PubMed:22543870, ECO:0000269|PubMed:2277041, ECO:0000269|PubMed:2558046, ECO:0000269|PubMed:2656684, ECO:0000269|PubMed:2668281, ECO:0000269|PubMed:2668953, ECO:0000269|PubMed:2674113, ECO:0000269|PubMed:28256224, ECO:0000269|PubMed:29138484, ECO:0000269|PubMed:2997120, ECO:0000269|PubMed:3536870}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ENVZ-CPLX|complex.ecocyc.ENVZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-ENVZ|complex.ecocyc.PHOSPHO-ENVZ]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3404|gene.b3404]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEJ4`
- `KEGG:ecj:JW3367;eco:b3404;ecoc:C3026_18470;`
- `GeneID:93778594;947272;`
- `GO:GO:0000155; GO:0000160; GO:0004721; GO:0005524; GO:0005829; GO:0005886; GO:0006970; GO:0007165; GO:0030288; GO:0042802; GO:0042803; GO:0046777`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase EnvZ (EC 2.7.13.3) (Osmolarity sensor protein EnvZ)
