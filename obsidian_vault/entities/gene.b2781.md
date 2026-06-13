---
entity_id: "gene.b2781"
entity_type: "gene"
name: "mazG"
source_database: "NCBI RefSeq"
source_id: "gene-b2781"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2781"
  - "mazG"
---

# mazG

`gene.b2781`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2781`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mazG (gene.b2781) is a gene entity. It encodes mazG (protein.P0AEY3). Encoded protein function: FUNCTION: Involved in the regulation of bacterial cell survival under conditions of nutritional stress. Regulates the type II MazE-MazF toxin-antitoxin (TA) system which mediates programmed cell death (PCD). This is achieved by lowering the cellular concentration of (p)ppGpp produced by RelA under amino acid starvation, thus protecting the cell from the toxicity of MazF. Reduction of (p)ppGpp can be achieved by direct degradation of (p)ppGpp or by degradation of NTPs, which are substrates for (p)ppGpp synthesis by RelA. {ECO:0000269|PubMed:16390452, ECO:0000269|PubMed:18353782, ECO:0000269|PubMed:20529853}. EcoCyc product frame: EG10572-MONOMER. Genomic coordinates: 2909894-2910685. EcoCyc protein note: MazG is a nucleoside pyrophosphohydrolase that limits the deleterious effect of the MazF toxin under nutritional stress conditions . MazF belongs to the superfamily of all-α NTP pyrophosphatases. Members of this family are predicted to perform "house-cleaning" functions by hydrolyzing non-canonical NTPs . MazG exhibits pyrophosphohydrolase activity toward all four dNTPs and also exhibits (somewhat less) activity toward all four rNTPs . Hydrolysis of GTP is more efficient that hydrolysis of ATP . Addition of purified MazEF proteins causes inhibition of MazG enzymatic activity...

## Biological Role

Repressed by mazE (protein.P0AE72). Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEY3|protein.P0AEY3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=mazG; function=+
- `represses` <-- [[protein.P0AE72|protein.P0AE72]] `RegulonDB` `S` - regulator=MazE; target=mazG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009117,ECOCYC:EG10572,GeneID:947254`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2909894-2910685:-; feature_type=gene
