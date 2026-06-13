---
entity_id: "gene.b3006"
entity_type: "gene"
name: "exbB"
source_database: "NCBI RefSeq"
source_id: "gene-b3006"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3006"
  - "exbB"
---

# exbB

`gene.b3006`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3006`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

exbB (gene.b3006) is a gene entity. It encodes exbB (protein.P0ABU7). Encoded protein function: FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates. Protects ExbD from proteolytic degradation and functionally stabilizes TonB. EcoCyc product frame: EG10271-MONOMER. Genomic coordinates: 3151250-3151984. EcoCyc protein note: ExbB is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and certain cofactors across the outer membrane. ExbB affects the stability of TonB and disruption of exbB (exbB::Tn10) results in decreased TonB function . ExbB is an inner membrane protein . ExbB interacts with ExbD and TonB . Topology analysis suggests that ExbB contains three transmembrane (TM) regions with the N-terminus in the periplasm and the C-terminus in the cytoplasm . ExbB forms multimers in vitro and in vivo . A large cytoplasmic loop (residues 40-129) is essential for Ton system function; expression of ExbB proteins with sequential 10-residue deletions in the cytoplasmic loop results in (reversible) growth arrest (that is not due to collapse of the PMF) . ExbB transmembrane domains do not participate in a proton translocation pathway...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABU7|protein.P0ABU7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=exbB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009869,ECOCYC:EG10271,GeneID:945420`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3151250-3151984:-; feature_type=gene
