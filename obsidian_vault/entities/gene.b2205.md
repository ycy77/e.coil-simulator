---
entity_id: "gene.b2205"
entity_type: "gene"
name: "napG"
source_database: "NCBI RefSeq"
source_id: "gene-b2205"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2205"
  - "napG"
---

# napG

`gene.b2205`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2205`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napG (gene.b2205) is a gene entity. It encodes napG (protein.P0AAL3). Encoded protein function: FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}. EcoCyc product frame: NAPG-MONOMER. EcoCyc synonyms: yojA, yojB. Genomic coordinates: 2299565-2300260. EcoCyc protein note: The EG12064 gene, which is located in the operon of the periplasmic nitrite reductase, encodes a ferredoxin-type non-heme iron-sulfur protein . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain incapable of producing menaquinone. Since experiments with a bacterial two-hybrid system showed that NapH interacts with NapC, it was concluded that NapG and NapH are required for electron transfer from ubiquinol, but not menaquinol, via EG12060 NapC, to the NAP-CPLX NapAB complex...

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAL3|protein.P0AAL3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napG; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napG; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napG; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napG; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napG; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napG; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007287,ECOCYC:EG12064,GeneID:945544`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2299565-2300260:-; feature_type=gene
