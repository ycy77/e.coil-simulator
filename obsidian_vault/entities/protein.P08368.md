---
entity_id: "protein.P08368"
entity_type: "protein"
name: "creB"
source_database: "UniProt"
source_id: "P08368"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "creB yjjE b4398 JW4361"
---

# creB

`protein.P08368`

## Static

- Type: `protein`
- Source: `UniProt:P08368`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation. CreB "Carbon source responsive response regulator," is a DNA-binding transcriptional dual regulator and belongs to the CreBC two-component system (TCS) , which controls genes involved in acetate and ribose metabolism, in the maltose regulon , in the pentose phosphate pathway , and genes which repair DNA damage associated with the replication fork . CreBC regulates the expression of cre regulon genes in response to a switch from complex to minimal medium . It is active when cells are fermenting glycolytic carbon sources. Induction of the cre regulon during pyruvate growth is entirely CreC dependent . CreBC is considered a global regulator that is positioned at the heart of metabolic control . CreB and CreC are part of the creABCD operon . CreB binds in vitro to a TTCACnnnnnnTTCAC sequence called the cre tag direct repeat, which stimulates the cre regulon . CreBC (TCS) is homologous (60-70%) with BrlAB of Aeromonas spp. at the amino acid level . CreC can act as the the phosphate donor for PhoB in PhoR mutants ( and references therein) but this activity is masked in PhoR+ strains and the CreC/PhoB pathway is not responsive to phosphate levels . A model of regulation by CreBC was proposed by Cariss et al...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `activates` --> [[gene.b4400|gene.b4400]] `RegulonDB` `S` - regulator=CreB; target=creD; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b4398|gene.b4398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08368`
- `KEGG:ecj:JW4361;eco:b4398;ecoc:C3026_23765;`
- `GeneID:948922;`
- `GO:GO:0000156; GO:0000976; GO:0000987; GO:0005829; GO:0006355; GO:0032993; GO:0042802; GO:0045893`

## Notes

Transcriptional regulatory protein CreB
