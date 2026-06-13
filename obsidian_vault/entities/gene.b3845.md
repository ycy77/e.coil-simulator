---
entity_id: "gene.b3845"
entity_type: "gene"
name: "fadA"
source_database: "NCBI RefSeq"
source_id: "gene-b3845"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3845"
  - "fadA"
---

# fadA

`gene.b3845`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3845`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadA (gene.b3845) is a gene entity. It encodes fadA (protein.P21151). Encoded protein function: FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Involved in the aerobic and anaerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629}. EcoCyc product frame: FADA-MONOMER. EcoCyc synonyms: oldA. Genomic coordinates: 4027609-4028772. EcoCyc protein note: 3-ketoacyl-CoA thiolase (FadA) is involved in the degradation of fatty acids via the β-oxidation cycle. The enzyme acts on 3-oxoacyl-CoAs in the presence of a CoA acceptor to produce acetyl-CoA and an acyl-CoA shortened by two carbon atoms. FadA has broad chain-length specificity for substrates, but exhibits its highest activity with medium-chain substrates. FadA and FadB form a multifunctional enzyme complex (data from E. coli B in ). Overexpression of FadA and FadB can be utilized for the production of long-chain fatty acids in an engineered reversal of the β-oxidation cycle . In the reverse direction the enzyme acts on an acyl-CoA and acetyl-CoA, catalyzing a non-decarboxylative Claisen condensation reaction that forms a 3-oxo-acyl-CoA elongated by two carbons...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21151|protein.P21151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fadA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=fadA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012562,ECOCYC:EG10278,GeneID:948324`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4027609-4028772:-; feature_type=gene
