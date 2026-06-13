---
entity_id: "gene.b3603"
entity_type: "gene"
name: "lldP"
source_database: "NCBI RefSeq"
source_id: "gene-b3603"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3603"
  - "lldP"
---

# lldP

`gene.b3603`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3603`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lldP (gene.b3603) is a gene entity. It encodes lldP (protein.P33231). Encoded protein function: FUNCTION: Uptake of L-lactate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport D-lactate and glycolate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}. EcoCyc product frame: LCTP-MONOMER. EcoCyc synonyms: lct, lctP. Genomic coordinates: 3777399-3779054. EcoCyc protein note: LldP is an inner membrane permease that functions in the the uptake of L-lactate, D-lactate and glycolate . The lldP gene is located in a lactate-inducible operon with the lldD and lldR genes encoding a lactate dehydrogenase and a regulatory protein, respectively . E.coli strains lacking both 2-hydroxymonocarboxylate transporters LldP and B2975-MONOMER "GlcA" are unable to grow with D-lactate, L-lactate or glyoxylate as sole carbon source. Overexpression of a plasmid carrying lldP restores growth of the double mutant on all three substrates . Transport is abolished by addition of the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . Disruption of the lld operon decreased lactate transport, which could be restored by complementation with the cloned lldP gene...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lldR (protein.P0ACL7), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579), lldR (protein.P0ACL7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33231|protein.P33231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lldP; function=+
- `activates` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldP; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=lldP; function=-
- `represses` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldP; function=-+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=lldP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011777,ECOCYC:EG11961,GeneID:948114`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3777399-3779054:+; feature_type=gene
