---
entity_id: "gene.b4168"
entity_type: "gene"
name: "tsaE"
source_database: "NCBI RefSeq"
source_id: "gene-b4168"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4168"
  - "tsaE"
---

# tsaE

`gene.b4168`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4168`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsaE (gene.b4168) is a gene entity. It encodes tsaE (protein.P0AF67). Encoded protein function: FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaB. TsaE seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. Displays ATPase activity in vitro. {ECO:0000269|PubMed:22378793}. EcoCyc product frame: EG11757-MONOMER. EcoCyc synonyms: yjeE. Genomic coordinates: 4395585-4396046. EcoCyc protein note: TsaE is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, EG11171-MONOMER TsaD, G6991-MONOMER TsaB, and TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network. TsaB can interact with both TsaE and TsaD directly, and the interactions appear to be mutually exclusive . Purified TsaE forms a heterogeneous mixture of oligomers in vitro...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF67|protein.P0AF67]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tsaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013649,ECOCYC:EG11757,GeneID:948684`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4395585-4396046:+; feature_type=gene
