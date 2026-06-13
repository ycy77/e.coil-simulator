---
entity_id: "gene.b0891"
entity_type: "gene"
name: "lolA"
source_database: "NCBI RefSeq"
source_id: "gene-b0891"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0891"
  - "lolA"
---

# lolA

`gene.b0891`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0891`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lolA (gene.b0891) is a gene entity. It encodes lolA (protein.P61316). Encoded protein function: FUNCTION: Participates in the translocation of lipoproteins from the inner membrane to the outer membrane. Only forms a complex with a lipoprotein if the residue after the N-terminal Cys is not an aspartate (The Asp acts as a targeting signal to indicate that the lipoprotein should stay in the inner membrane); the inner membrane retention signal functions at the release step. {ECO:0000269|PubMed:11758943}.; FUNCTION: May act as a regulator of the RCS-phosphorelay signal transduction pathway. {ECO:0000269|PubMed:11758943}. EcoCyc product frame: G6465-MONOMER. EcoCyc synonyms: yzzV, lplA. Genomic coordinates: 937372-937983. EcoCyc protein note: LolA is a periplasmic chaperone which transports lipoproteins from the inner membrane (IM) to the outer membrane (OM); LolA is part of the 5-protein LolABCDE lipoprotein trafficking pathway; LolA receives lipoproteins destined for the outer membrane* from the IM ABC-62-CPLX "LolCDE release complex" and delivers them to the OM lipoprotein EG11293-MONOMER "LolB" for insertion into the OM...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61316|protein.P61316]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lolA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003031,ECOCYC:G6465,GeneID:948989`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:937372-937983:+; feature_type=gene
