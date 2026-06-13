---
entity_id: "gene.b0096"
entity_type: "gene"
name: "lpxC"
source_database: "NCBI RefSeq"
source_id: "gene-b0096"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0096"
  - "lpxC"
---

# lpxC

`gene.b0096`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0096`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxC (gene.b0096) is a gene entity. It encodes lpxC (protein.P0A725). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of UDP-3-O-myristoyl-N-acetylglucosamine to form UDP-3-O-myristoylglucosamine and acetate, the committed step in lipid A biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00388, ECO:0000269|PubMed:10026271, ECO:0000269|PubMed:8530464, ECO:0000269|PubMed:8824222, ECO:0000269|Ref.7}. EcoCyc product frame: UDPACYLGLCNACDEACETYL-MONOMER. EcoCyc synonyms: asmB, envA. Genomic coordinates: 106557-107474. EcoCyc protein note: EC-3.5.1.108 (LpxC) catalyzes the second reaction and the first committed step in lipid A biosynthesis. LpxC hydrolyzes UDP-3-O-(3-hydroxymyristoyl)-N-acetlyglucosamine to UDP-3-O-(3-hydroxymyristoyl)glucosamine and acetate . The mechanism of action of LpxC has been studied, and a high-throughput fluorescent screen as well as a mass-spectrometry based screen have been developed to evaluate LpxC activity . LpxC is a metalloenzyme that was reported to require bound zinc for activity . Site-directed mutagenesis has identified zinc binding sites . More recently, LpxC with bound iron was shown to have higher activity than zinc-bound enzyme . While LpxC has significantly higher affinity for zinc, in vivo concentrations of readily available iron are higher that those of zinc...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186). Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A725|protein.P0A725]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=lpxC; function=+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=lpxC; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=lpxC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000336,ECOCYC:EG10265,GeneID:944816`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:106557-107474:+; feature_type=gene
