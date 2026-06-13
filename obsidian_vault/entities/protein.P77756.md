---
entity_id: "protein.P77756"
entity_type: "protein"
name: "queC"
source_database: "UniProt"
source_id: "P77756"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queC ybaX b0444 JW0434"
---

# queC

`protein.P77756`

## Static

- Type: `protein`
- Source: `UniProt:P77756`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent conversion of 7-carboxy-7-deazaguanine (CDG) to 7-cyano-7-deazaguanine (preQ(0)). {ECO:0000250, ECO:0000269|PubMed:16199558}. QueC appears to be the 7-cyano-7-deazaguanine synthase that catalyzes an early step of queuosine biosynthesis, leading from GTP to the formation of preQ0 . Queuosine is one of the most complex tRNA modifications, occurring at the wobble position of the GUN anticodon in the Asn, Asp, Tyr, and His tRNAs. queC rescues the queuosine deficiency phenotype of a mutant E. coli B strain . The biochemical activity of QueC was studied using the orthologous BSU13720-MONOMER from TAX-1423 .

## Biological Role

Catalyzes RXN-12093 (reaction.ecocyc.RXN-12093).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent conversion of 7-carboxy-7-deazaguanine (CDG) to 7-cyano-7-deazaguanine (preQ(0)). {ECO:0000250, ECO:0000269|PubMed:16199558}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12093|reaction.ecocyc.RXN-12093]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0444|gene.b0444]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77756`
- `KEGG:ecj:JW0434;eco:b0444;ecoc:C3026_02175;`
- `GeneID:947034;`
- `GO:GO:0005524; GO:0008270; GO:0008616; GO:0016879`
- `EC:6.3.4.20`

## Notes

7-cyano-7-deazaguanine synthase (EC 6.3.4.20) (7-cyano-7-carbaguanine synthase) (PreQ(0) synthase) (Queuosine biosynthesis protein QueC)
