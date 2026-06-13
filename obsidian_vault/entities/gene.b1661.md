---
entity_id: "gene.b1661"
entity_type: "gene"
name: "cfa"
source_database: "NCBI RefSeq"
source_id: "gene-b1661"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1661"
  - "cfa"
---

# cfa

`gene.b1661`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1661`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cfa (gene.b1661) is a gene entity. It encodes cfa (protein.P0A9H7). Encoded protein function: FUNCTION: Transfers a methylene group from S-adenosyl-L-methionine to the cis double bond of an unsaturated fatty acid chain resulting in the replacement of the double bond with a methylene bridge. {ECO:0000250}. EcoCyc product frame: CFA-MONOMER. EcoCyc synonyms: cdfA. Genomic coordinates: 1741413-1742561. EcoCyc protein note: Cyclopropane fatty acyl phospholipid synthase (CFA) catalyzes a modification of the acyl chains of phospholipid bilayers through methylenation of unsaturated fatty acyl chains to their cyclopropane derivatives . It is one of the few enzymes known to act on the nonpolar portion of phospholipids dispersed in a vesicle. The enzyme acts on the double bond of a phospholipid unsaturated fatty acid residue, which must be 9-11 carbon atoms removed from the glycerol backbone of the molecule. Studies using analogs of S-adenosyl-L-methionine suggest that the reaction proceeds via methyl transfer followed by proton loss . CFA synthase is thought to operate via a carbocation mechanism . The presence of a bicarbonate ion in the active site was predicted by similarity to the M. tuberculosis cyclopropane synthases. The presence of bicarbonate enhances the Vmax of CFA synthase 3-fold...

## Biological Role

Repressed by cpxQ (gene.b4716), nac (protein.Q47005). Activated by rydC (gene.b4597), arrS (gene.b4704), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9H7|protein.P0A9H7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=cfa; function=+
- `activates` <-- [[gene.b4704|gene.b4704]] `RegulonDB` `S` - regulator=ArrS; target=cfa; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cfa; function=+
- `represses` <-- [[gene.b4716|gene.b4716]] `RegulonDB` `S` - regulator=CpxQ; target=cfa; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cfa; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005555,ECOCYC:EG11531,GeneID:944811`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1741413-1742561:+; feature_type=gene
