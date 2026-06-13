---
entity_id: "protein.P77718"
entity_type: "protein"
name: "thiI"
source_database: "UniProt"
source_id: "P77718"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiI yajK b0423 JW0413"
---

# thiI

`protein.P77718`

## Static

- Type: `protein`
- Source: `UniProt:P77718`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent transfer of a sulfur to tRNA to produce 4-thiouridine in position 8 of tRNAs, which functions as a near-UV photosensor. Also catalyzes the transfer of sulfur to the sulfur carrier protein ThiS, forming ThiS-thiocarboxylate. This is a step in the synthesis of thiazole, in the thiamine biosynthesis pathway. The sulfur is donated as persulfide by IscS. {ECO:0000269|PubMed:10722656, ECO:0000269|PubMed:10753862, ECO:0000269|PubMed:18604845}. ThiI is a bifunctional enzyme that is required both for the conversion of uridine to 4-thiouridine (s4U) at position 8 in certain tRNAs and for the synthesis of the thiazole moiety of thiamine. The protien contains several functional domains - an N-terminal ferredoxin-like domain (NFLD), a THUMP (THioUridine synthases, RNA Methylases and Pseudouridine synthases) domain, a PP-loop-containing pyrophosphatase domain (the catalytic domain), and a rhodanese domain. The THUMP domain is known to specifically interact with tRNAs that are modified at position 6, 8 or 10 . The PP-loop motif binds ATP, which allows the formation of an adenylated tRNA intermediate , and the rhodanese domain is involved in sulfur transfer . Mutants in the biosynthesis of s4U-modified tRNA were initially identified by their easily selectable phenotype, e.g....

## Biological Role

Catalyzes RXN-18388 (reaction.ecocyc.RXN-18388), RXN-9788 (reaction.ecocyc.RXN-9788). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent transfer of a sulfur to tRNA to produce 4-thiouridine in position 8 of tRNAs, which functions as a near-UV photosensor. Also catalyzes the transfer of sulfur to the sulfur carrier protein ThiS, forming ThiS-thiocarboxylate. This is a step in the synthesis of thiazole, in the thiamine biosynthesis pathway. The sulfur is donated as persulfide by IscS. {ECO:0000269|PubMed:10722656, ECO:0000269|PubMed:10753862, ECO:0000269|PubMed:18604845}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-18388|reaction.ecocyc.RXN-18388]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9788|reaction.ecocyc.RXN-9788]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0423|gene.b0423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77718`
- `KEGG:ecj:JW0413;eco:b0423;ecoc:C3026_02065;`
- `GeneID:86862968;945067;`
- `GO:GO:0000049; GO:0002937; GO:0004810; GO:0005524; GO:0005829; GO:0009228; GO:0009229; GO:0009589; GO:0016783; GO:0019448; GO:0052837; GO:0097163; GO:0140741; GO:1990221; GO:1990228`
- `EC:2.8.1.4`

## Notes

tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine synthase)
