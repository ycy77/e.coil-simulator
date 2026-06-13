---
entity_id: "gene.b1518"
entity_type: "gene"
name: "lsrG"
source_database: "NCBI RefSeq"
source_id: "gene-b1518"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1518"
  - "lsrG"
---

# lsrG

`gene.b1518`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1518`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrG (gene.b1518) is a gene entity. It encodes lsrG (protein.P64461). Encoded protein function: FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the conversion of (4S)-4-hydroxy-5-phosphonooxypentane-2,3-dione (P-DPD) to 3-hydroxy-5-phosphonooxypentane-2,4-dione (P-HPD). {ECO:0000255|HAMAP-Rule:MF_02051, ECO:0000269|PubMed:17274596, ECO:0000269|PubMed:21454635}. EcoCyc product frame: G6805-MONOMER. EcoCyc synonyms: yneC. Genomic coordinates: 1606999-1607289. EcoCyc protein note: LsrG is an enzyme involved in the degradation of the quorum-sensing regulator Autoinducer 2 (AI-2). Purified LsrG degrades CPD-10551 phospho-AI-2 (4-hydroxy-2,3-pentanedione 5-phosphate) . The reaction products were later shown to be a mixture of CPD0-2467 (P-HPD) and CPD0-2468 (P-TPO); CPD0-2466 was proposed to be a reaction intermediate . It is now thought that LsrG catalyzes the isomerization reaction from phospho-AI-2 to P-HPD, and that P-HPD exists in equilibrium with its hydrated form, P-TPO . A crystal structure of the enzyme has been solved at 1.8 Å resolution. Mutants in predicted active site residues N25, E54, H65, H70 have reduced or no catalytic activity in vitro . LsrG: "luxS regulated"

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8), glaR (protein.P37338).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64461|protein.P64461]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrG; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=lsrG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005067,ECOCYC:G6805,GeneID:946073`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1606999-1607289:+; feature_type=gene
