---
entity_id: "gene.b2155"
entity_type: "gene"
name: "cirA"
source_database: "NCBI RefSeq"
source_id: "gene-b2155"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2155"
  - "cirA"
---

# cirA

`gene.b2155`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2155`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cirA (gene.b2155) is a gene entity. It encodes cirA (protein.P17315). Encoded protein function: FUNCTION: Not yet known. Postulated to participate in iron transport. Outer membrane receptor for colicins IA and IB. EcoCyc product frame: EG10155-MONOMER. EcoCyc synonyms: cir, feuA. Genomic coordinates: 2244778-2246769. EcoCyc protein note: Cir is a member of the Outer Membrane Receptor (OMR) family of porins. Cir is a TonB-dependent iron-siderophore complex uptake receptor . The substrate spectrum of Cir is very similar to that of Fiu. Cir transports monomers, dimers and linear trimers of 2,3-dihydroxybenzoylserine . Cir transports the ferric dicatecholate CPD-21612 Fe(DHBS)2 and the siderophore cephalosporin, CPD-28221 . Cir is also a receptor for colicins IA, IB, and V and microcins E492, H47, and M . Cir acts as both the receptor and translocator for colicin IA . Crystal structures of Cir alone and in complex with the receptor domain of colicin IA have been reported . The class IIb microcin MccM targets the TonB-dependent siderophore receptors G6414-MONOMER Fiu, CirA, and EG10293-MONOMER FepA for entry. Expression of CirA is posttranscriptionally regulated by several small RNAs as well as by Hfq. Outer membrane protein (OMP) localisation and turnover has been studied using labelled, modified colicin 1a which forms a complex with Cir but is blocked for import...

## Biological Role

Repressed by Hfq (complex.ecocyc.CPLX0-1461), [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), omrA (gene.b4444), omrB (gene.b4445), hfq (protein.P0A6X3), fur (protein.P0A9A9). Activated by ryhB (gene.b4451), rpoD (protein.P00579), ygaV (protein.P77295).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17315|protein.P17315]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=cirA; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cirA; function=+
- `activates` <-- [[protein.P77295|protein.P77295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-1461|complex.ecocyc.CPLX0-1461]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=cirA; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=cirA; function=-
- `represses` <-- [[protein.P0A6X3|protein.P0A6X3]] `RegulonDB` `S` - regulator=Hfq; target=cirA; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=cirA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007126,ECOCYC:EG10155,GeneID:949042`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2244778-2246769:-; feature_type=gene
