---
entity_id: "protein.P23827"
entity_type: "protein"
name: "eco"
source_database: "UniProt"
source_id: "P23827"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eco eti b2209 JW2197"
---

# eco

`protein.P23827`

## Static

- Type: `protein`
- Source: `UniProt:P23827`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: General inhibitor of pancreatic serine proteases: inhibits chymotrypsin, trypsin, elastases, factor X, kallikrein as well as a variety of other proteases. The strength of inhibition does not appear to be correlated with a particular protease specificity. {ECO:0000269|PubMed:35483450}. Ecotin inhibits trypsin and a number of additional heterologous proteases . Some endogenous E. coli proteases are not sensitive to ecotin . Residue Met84 is the reactive site . M84K, M84R, and M84L mutant proteins exhibit altered substrate specificity . The activities of various mutant proteins have been evaluated . Ecotin is implicated in defense from T6SS-mediated killing by TAX-666 . Knockout mutant and crystal structural studies of ecotin interacting with mannan-binding lectin-associated serine proteases (MASPs), components of the lectin pathway of the complement system, revealed ecotin's activity as a microbial defense factor and how binding sites 1 and 2 contribute to ecotin's inhibition of MASP enzymes, thus providing a potential antibiotic target . Ecotin is a homodimer ; each homodimer binds to two protease monomers . The dimerization and substrate interaction regions have been examined in detail . Ecotin is periplasmic . Ecotin exhibits anticoagulant properties...

## Biological Role

Component of serine protease inhibitor ecotin (complex.ecocyc.CPLX0-1441).

## Annotation

FUNCTION: General inhibitor of pancreatic serine proteases: inhibits chymotrypsin, trypsin, elastases, factor X, kallikrein as well as a variety of other proteases. The strength of inhibition does not appear to be correlated with a particular protease specificity. {ECO:0000269|PubMed:35483450}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1441|complex.ecocyc.CPLX0-1441]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2209|gene.b2209]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23827`
- `KEGG:ecj:JW2197;eco:b2209;ecoc:C3026_12345;`
- `GeneID:946700;`
- `GO:GO:0004867; GO:0006952; GO:0030288; GO:0042803`

## Notes

Ecotin
