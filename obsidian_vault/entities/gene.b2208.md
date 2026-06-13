---
entity_id: "gene.b2208"
entity_type: "gene"
name: "napF"
source_database: "NCBI RefSeq"
source_id: "gene-b2208"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2208"
  - "napF"
---

# napF

`gene.b2208`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2208`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napF (gene.b2208) is a gene entity. It encodes napF (protein.P0AAL0). Encoded protein function: FUNCTION: Could be involved in the maturation of NapA, the catalytic subunit of the periplasmic nitrate reductase, before its export into the periplasm (PubMed:17074894). Is not involved in the electron transfer from menaquinol or ubiquinol to the periplasmic nitrate reductase (PubMed:11967083). {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:17074894}. EcoCyc product frame: NAPF-MONOMER. EcoCyc synonyms: yojG. Genomic coordinates: 2303003-2303497. EcoCyc protein note: The napF gene encodes a predicted 3Fe-4S iron sulfur protein that is not essential for the activity of periplasmic nitrate reductase (Nap), but contributes to the maximum rate of nitrate reduction . NapF does not appear to be involved in the electron transfer from menaquinol or ubiquinol to NAP-CPLX . Loss of NapF alone causes a growth defect under anaerobic conditions on glycerol/nitrate medium; concurrent loss of NapG and NapH suppresses that defect. However, loss of NapF does not significantly affect nitrate reduction rates; it may therefore play a role in energy conservation rather than a direct role in nitrate reduction . NapF is located in the cytoplasm, and it can interact directly with NapA, which is exported to the periplasm via the Tat pathway. This indicates a possible role for NapF during NapA maturation...

## Biological Role

Repressed by lrp (protein.P0ACJ0), narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAL0|protein.P0AAL0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napF; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napF; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napF; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napF; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napF; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napF; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007293,ECOCYC:EG12068,GeneID:946813`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2303003-2303497:-; feature_type=gene
