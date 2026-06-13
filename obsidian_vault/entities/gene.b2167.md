---
entity_id: "gene.b2167"
entity_type: "gene"
name: "fruA"
source_database: "NCBI RefSeq"
source_id: "gene-b2167"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2167"
  - "fruA"
---

# fruA

`gene.b2167`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2167`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fruA (gene.b2167) is a gene entity. It encodes fruA (protein.P20966). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000269|PubMed:8626640, ECO:0000305|PubMed:3076173}. EcoCyc product frame: FRUA-MONOMER. EcoCyc synonyms: ptsF. Genomic coordinates: 2259719-2261410. EcoCyc protein note: fruA expressed in trans restores the ability of a fruA transposon mutant to grow on 2.5mM fructose as carbon source and to phosphorylate fructose in vitro. FruA is predicted to be an inner membrane protein . FruA lacking the B' domain is able to transport fructose in vivo and to phosphorylate fructose in vitro. FruA lacking the B' domain shows less affinity for FruB in vitro. Loss of the B' domain mainly affects phosphoryl transfer between FruB which contains the pseudo-HPr domain and FruA . FruA containing a C112S amino acid substitution is unable to transport fructose in vivo or in vitro. The IIC domain of FruA is predicted to contain 9 transmembrane segments. FruA is likely to function as a homo-oligomer...

## Biological Role

Repressed by cra (protein.P0ACP1).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P20966|protein.P20966]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=fruA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007172,ECOCYC:EG10336,GeneID:946672`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2259719-2261410:-; feature_type=gene
