---
entity_id: "gene.b0524"
entity_type: "gene"
name: "lpxH"
source_database: "NCBI RefSeq"
source_id: "gene-b0524"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0524"
  - "lpxH"
---

# lpxH

`gene.b0524`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0524`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxH (gene.b0524) is a gene entity. It encodes lpxH (protein.P43341). Encoded protein function: FUNCTION: Hydrolyzes the pyrophosphate bond of UDP-2,3-diacylglucosamine to yield 2,3-diacylglucosamine 1-phosphate (lipid X) and UMP by catalyzing the attack of water at the alpha-P atom (PubMed:12000770). Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell (PubMed:12000770, PubMed:12000771). Is essential for E.coli growth (PubMed:12000771). Does not cleave the unacylated UDP-GlcNAc, the mono-acylated UDP-3-O-(R)-3-hydroxymyristoyl-GlcNAc, and CDP-diacylglycerol (PubMed:12000770). {ECO:0000269|PubMed:12000770, ECO:0000269|PubMed:12000771}. EcoCyc product frame: EG12666-MONOMER. EcoCyc synonyms: ybbF. Genomic coordinates: 553218-553940. EcoCyc protein note: UDP-2,3-diacylglucosamine hydrolase (LpxH) catalyzes the fourth step in lipid A synthesis, hydrolyzing UDP-2,3-bis(3-hydroxymyristoyl)glucosamine to yield 2,3-bis(3-hydroxymyristoyl)-β-D-glucosaminyl 1-phosphate (lipid X) . LpxH is a peripheral membrane protein whose activity appears to be stimulated by Mn2+ in vitro. LpxH catalyzes the attack of water on the α-P atom of the UDP moiety to form lipid X and UMP...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43341|protein.P43341]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lpxH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001804,ECOCYC:EG12666,GeneID:949053`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:553218-553940:-; feature_type=gene
