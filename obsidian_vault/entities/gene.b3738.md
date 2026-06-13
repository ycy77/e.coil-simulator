---
entity_id: "gene.b3738"
entity_type: "gene"
name: "atpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3738"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3738"
  - "atpB"
---

# atpB

`gene.b3738`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3738`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpB (gene.b3738) is a gene entity. It encodes atpB (protein.P0AB98). Encoded protein function: FUNCTION: Key component of the proton channel; it plays a direct role in the translocation of protons across the membrane. EcoCyc product frame: ATPB-MONOMER. EcoCyc synonyms: papD, uncB. Genomic coordinates: 3921236-3922051. EcoCyc protein note: Subunit-a of the Fo complex is an integral membrane protein that plays a critical role in the proton translocation mechanism. Subunit-a is thought to provide aqueous access channels to and from the H+ binding site that is located in the decameric c-ring . Subunit-a contains 5 transmembrane helices (TMH); the amino terminus is located in the periplasm and the carboxy terminus is located in the cytoplasm . Mutational and cross-linking studies indicate that transmembrane helices 2,3,4 and 5 form a four helix bundle that interacts with subunit c. pH-dependent conformational change of helices 4 and 5 has been implicated in the gating of H+ . Structural divergence of the c-subunit ring and the a-subunits between bacterial species may allow development of species specific drugs which target these subunits . Reviews:

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB98|protein.P0AB98]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012222,ECOCYC:EG10099,GeneID:948252`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3921236-3922051:-; feature_type=gene
