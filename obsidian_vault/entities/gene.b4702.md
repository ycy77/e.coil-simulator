---
entity_id: "gene.b4702"
entity_type: "gene"
name: "mgtL"
source_database: "NCBI RefSeq"
source_id: "gene-b4702"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4702"
  - "mgtL"
---

# mgtL

`gene.b4702`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4702`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgtL (gene.b4702) is a gene entity. It encodes mgtL (protein.E2JKY7). Encoded protein function: FUNCTION: Makes mgtA transcription sensitive to intracellular proline levels. Under low levels of proline this protein cannot be fully translated, and a stem loop forms which permits transcription of the downstream mgtA gene (By similarity). {ECO:0000250}. EcoCyc product frame: MONOMER0-4201. Genomic coordinates: 4467431-4467484. EcoCyc protein note: MgtL functions as a leader peptide, affecting the expression of MgtA in response to magnesium ion levels . The MgtL peptide contains an N-terminal region that acts as a translation-aborting sequence. Mutations that change the residues EPDP, and in particular the acidic residues E and D, lead to increased translation through this region, while translation aborts more frequently in a ΔEG10889 rpmE strain. Both in vitro and in vivo, addition of increasing levels of Mg2+ lead to a decrease in aborted translation of MgtL. This effect is dependent on the presence of the N-terminal MEPDPT sequence and RpmE. Thus, the N-terminal region of MgtL appears to act as an intrinsic ribosome-destabilizing element. Translation of MgtA is directly correlated with aborted translation of MgtL...

## Biological Role

Activated by rpoD (protein.P00579), phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.E2JKY7|protein.E2JKY7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mgtL; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `C` - regulator=PhoP; target=mgtL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285267,ECOCYC:G0-10689,GeneID:9797237`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4467431-4467484:+; feature_type=gene
