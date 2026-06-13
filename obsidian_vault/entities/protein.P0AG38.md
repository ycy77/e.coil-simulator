---
entity_id: "protein.P0AG38"
entity_type: "protein"
name: "rhtC"
source_database: "UniProt"
source_id: "P0AG38"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhtC yigJ b3823 JW5586"
---

# rhtC

`protein.P0AG38`

## Static

- Type: `protein`
- Source: `UniProt:P0AG38`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Conducts the efflux of threonine. {ECO:0000269|PubMed:10386596}. RhtC can mediate the export of L-threonine; the physiological role of the transporter remains uncertain. Multicopy expression of rhtC confers resistance to high levels of threonine (50mg/mL) . Multicopy expression of rhtC confers increased resistance to L-threonine but not to D-threonine, L-homoserine, D-homoserine, L-homoserine lactone nor a range of other amino acids (see also ). Overexpression of rhtC increases threonine production in E. coli threonine producer strains ; heterologous expression of rhtC increases L-threonine production in Corynebacterium glutamicum threonine producing strains . RhtC is homologous to RHTB-MONOMER "RhtB"; proteins with homolgy to RhtB occur in a wide range of prokaryotes and form a family of putative transporters that mediate metabolite export . RhtC is a member of the Resistance to Homoserine/Threonine (RhtB) Family of transporters within the LysE superfamily; RhtC is a probable substrate:H+ antiporter . RhtC is predicted to be an inner membrane protein with 5 transmembrane domains; experimental topology analysis suggests the C-terminus is located in the cytoplasm rht: resistance to homoserine and threonine

## Biological Role

Catalyzes L-threonine:proton antiport (reaction.ecocyc.TRANS-RXN0-0244).

## Annotation

FUNCTION: Conducts the efflux of threonine. {ECO:0000269|PubMed:10386596}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-0244|reaction.ecocyc.TRANS-RXN0-0244]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3823|gene.b3823]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG38`
- `KEGG:ecj:JW5586;eco:b3823;ecoc:C3026_20690;`
- `GeneID:75174059;948317;`
- `GO:GO:0005886; GO:0006865; GO:0015171; GO:0015565; GO:0015826`

## Notes

Threonine efflux protein
