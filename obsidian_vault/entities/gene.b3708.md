---
entity_id: "gene.b3708"
entity_type: "gene"
name: "tnaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3708"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3708"
  - "tnaA"
---

# tnaA

`gene.b3708`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3708`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tnaA (gene.b3708) is a gene entity. It encodes tnaA (protein.P0A853). Encoded protein function: Tryptophanase (EC 4.1.99.1) (L-tryptophan indole-lyase) (TNase) EcoCyc product frame: TRYPTOPHAN-MONOMER. EcoCyc synonyms: ind, tnaR. Genomic coordinates: 3888730-3890145. EcoCyc protein note: Tryptophanase or tryptophan indole-lyase (TnaA) is an extremely well-studied pyridoxal phosphate (PLP)-dependent enzyme that catalyzes the cleavage of L-tryptophan to indole, pyruvate and NH4+. Together with the tryptophan transporter TnaB, it enables utilization of L-tryptophan as sole source of nitrogen or carbon for growth. In recent years, it has become clear that one of the reaction products, indole, plays a significant role as an extracellular and intracellular signal, even acting as a cell cycle regulator . Indole production by TnaA depends directly on the amount of exogenous tryptophan, and the enzyme does not appear to degrade internal anabolic tryptophan . Tryptophanase is a major contributor towards the cellular L-cysteine desulfhydrase (CD) activity . In vitro, tryptophanase also catalyzes α,β elimination, β replacement, and α hydrogen exchange reactions with a variety of L-amino acids . Tryptophanase is one of the most S-sulfhydrated proteins in E. coli; at least six of its seven Cys residues can be S-sulfhydrated. S-sulfhydration reduces the enzymatic activity of tryptophanase...

## Biological Role

Repressed by rplD (protein.P60723), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), torR (protein.P38684).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A853|protein.P0A853]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tnaA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=tnaA; function=+
- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `S` - regulator=TorR; target=tnaA; function=+
- `represses` <-- [[protein.P60723|protein.P60723]] `RegulonDB|EcoCyc` `C` - regulator=RplD; target=tnaA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tnaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012133,ECOCYC:EG11005,GeneID:948221`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3888730-3890145:+; feature_type=gene
