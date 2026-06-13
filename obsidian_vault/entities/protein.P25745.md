---
entity_id: "protein.P25745"
entity_type: "protein"
name: "mnmA"
source_database: "UniProt"
source_id: "P25745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mnmA asuE trmU ycfB b1133 JW1119"
---

# mnmA

`protein.P25745`

## Static

- Type: `protein`
- Source: `UniProt:P25745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the 2-thiolation of uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln), leading to the formation of s(2)U34, the first step of tRNA-mnm(5)s(2)U34 synthesis. Sulfur is provided by IscS, via a sulfur-relay system. Binds ATP and its substrate tRNAs. {ECO:0000269|PubMed:12549933}. MnmA catalyzes formation of the 2-thiouridine modification of the modified nucleoside 5-methylamino-methyl-2-thiouridine (mnm5s2U34) in the wobble position of tRNAGln, tRNALys and tRNAGlu . A sulfur relay system consisting of IscS and the TusABCDE proteins is required for delivery of the sulfur atom . In vitro, a low level of MnmA activity on tRNAGlu could be achieved in the presence of Mg-ATP, cysteine, and the IscS cysteine desulfurase. The enzyme also shows activity toward anticodon stem-loop (tRNA fragment) substrates. MnmA binds to tRNALys and appears to bind to ATP . Crystal structures of MnmA together with tRNAGlu have been solved , revealing an adenylated tRNA intermediate and the basis for recognition of the specific tRNA substrates. Possible reaction mechanisms were proposed . While initially it was thought that MnmA activity does not depend on an iron-sulfur cluster, it was later shown that MnmA from TAX-562 can bind a [4Fe-4S] cluster, and that the binding is essential for sulfuration of U34-tRNA...

## Biological Role

Catalyzes RXN0-2023 (reaction.ecocyc.RXN0-2023). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the 2-thiolation of uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln), leading to the formation of s(2)U34, the first step of tRNA-mnm(5)s(2)U34 synthesis. Sulfur is provided by IscS, via a sulfur-relay system. Binds ATP and its substrate tRNAs. {ECO:0000269|PubMed:12549933}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2023|reaction.ecocyc.RXN0-2023]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1133|gene.b1133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25745`
- `KEGG:ecj:JW1119;eco:b1133;ecoc:C3026_06815;`
- `GeneID:75203719;945690;`
- `GO:GO:0000049; GO:0002143; GO:0005524; GO:0005829; GO:0016783; GO:0097532; GO:0103016; GO:1990228`
- `EC:2.8.1.13`

## Notes

tRNA-specific 2-thiouridylase MnmA (EC 2.8.1.13)
