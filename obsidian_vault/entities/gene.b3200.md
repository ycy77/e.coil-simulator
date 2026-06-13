---
entity_id: "gene.b3200"
entity_type: "gene"
name: "lptA"
source_database: "NCBI RefSeq"
source_id: "gene-b3200"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3200"
  - "lptA"
---

# lptA

`gene.b3200`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3200`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptA (gene.b3200) is a gene entity. It encodes lptA (protein.P0ADV1). Encoded protein function: FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. May form a bridge between the inner membrane and the outer membrane, via interactions with LptC and LptD, thereby facilitating LPS transfer across the periplasm. {ECO:0000255|HAMAP-Rule:MF_01914, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:18480051, ECO:0000269|PubMed:21169485}. EcoCyc product frame: YHBN-MONOMER. EcoCyc synonyms: yhbN. Genomic coordinates: 3343380-3343937. EcoCyc protein note: LptA is an essential periplasmic component of the Lpt lipopolysaccharide (LPS) transport system. Depletion of LptA results in impaired lipopolysaccharide transport to the outer membrane ; a conditional mutant which contains inactivating point mutations in LptA rapidly stops growing when incubated at the restrictive temperature and newly synthesized LPS appears trapped on the periplasmic side of the inner membrane . LptA drives a specific, protein mediated, long lived association between proteoliposomes containing LptBFGC and LPS and proteliposomes containing LptDE . Purified LptA binds smooth and rough LPS; purified LptA binds to the lipid A domain of LPS...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADV1|protein.P0ADV1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lptA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lptA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010510,ECOCYC:G7665,GeneID:947920`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3343380-3343937:+; feature_type=gene
