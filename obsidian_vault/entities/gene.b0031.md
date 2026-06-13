---
entity_id: "gene.b0031"
entity_type: "gene"
name: "dapB"
source_database: "NCBI RefSeq"
source_id: "gene-b0031"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0031"
  - "dapB"
---

# dapB

`gene.b0031`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0031`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dapB (gene.b0031) is a gene entity. It encodes dapB (protein.P04036). Encoded protein function: FUNCTION: Catalyzes the conversion of 4-hydroxy-tetrahydrodipicolinate (HTPA) to tetrahydrodipicolinate. Can use both NADH and NADPH as a reductant, with NADH being twice as effective as NADPH. {ECO:0000255|HAMAP-Rule:MF_00102, ECO:0000269|PubMed:20503968, ECO:0000269|PubMed:7893644}. EcoCyc product frame: DIHYDROPICRED-MONOMER. Genomic coordinates: 28374-29195. EcoCyc protein note: 4-hydroxy-tetrahydrodipicolinate reductase, historically called dihydrodipicolinate reductase (DHDPR, DapB) catalyzes a step in lysine biosynthesis via diaminopimelate. The substrate for DapB is (4S)-4-hydroxy-2,3,4,5-tetrahydro-(2S)-dipicolinate (HTPA) . Given the discovery of HTPA as the true substrate of DapB , previous data on the reaction mechanism of the enzyme, e.g. in , need to be re-evaluated. Crystal structures of the enzyme have been solved . The enzyme consists of two domains; the N-terminal domain binds the dinucleotide cosubstrate, while the C-terminal domain is thought to bind dihydrodipicolinate . Conformational change upon substrate binding may be essential for catalysis ; a reaction mechansim was proposed . Interactions of DapB with a variety of nucleotide substrates were investigated by isothermal titration calorimetry and crystallography...

## Biological Role

Repressed by fur (protein.P0A9A9), nac (protein.Q47005). Activated by rpoD (protein.P00579), argP (protein.P0A8S1).

## Enriched Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04036|protein.P04036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dapB; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `C` - regulator=ArgP; target=dapB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=dapB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dapB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000112,ECOCYC:EG10206,GeneID:944762`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:28374-29195:+; feature_type=gene
