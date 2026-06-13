---
entity_id: "gene.b1517"
entity_type: "gene"
name: "lsrF"
source_database: "NCBI RefSeq"
source_id: "gene-b1517"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1517"
  - "lsrF"
---

# lsrF

`gene.b1517`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1517`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrF (gene.b1517) is a gene entity. It encodes lsrF (protein.P76143). Encoded protein function: FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the transfer of an acetyl moiety from 3-hydroxy-5-phosphonooxypentane-2,4-dione to CoA to form glycerone phosphate and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_02052, ECO:0000269|PubMed:25225400}. EcoCyc product frame: G6804-MONOMER. EcoCyc synonyms: yneB. Genomic coordinates: 1606100-1606975. EcoCyc protein note: LsrF is the final enzyme in the pathway for degradation of the intercellular signaling molecule AI-2. It acts as a 3-hydroxy-2,4-pentadione 5-phosphate (P-HPD) thiolase, catalyzing the transfer of the acetyl group of P-HPD to coenzyme A . LsrF was noted to have similarity to class I aldolases , and the activity described in is novel for this family of enzymes. Kinetic measurements showed a positive Hill coefficient for both substrates, P-HPD and coenzyme A, indicating cooperativity . Crystal structures of LsrF were solved in both the apo form and in complex with phospho-AI-2 analogs. The protein is a homodecamer of (αβ)8 barrels with domain-swapped N termini, and the structure is similar to that of class I aldolases that process phosphorylated sugars...

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76143|protein.P76143]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrF; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005065,ECOCYC:G6804,GeneID:946071`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1606100-1606975:+; feature_type=gene
