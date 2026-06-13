---
entity_id: "gene.b0902"
entity_type: "gene"
name: "pflA"
source_database: "NCBI RefSeq"
source_id: "gene-b0902"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0902"
  - "pflA"
---

# pflA

`gene.b0902`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0902`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pflA (gene.b0902) is a gene entity. It encodes pflA (protein.P0A9N4). Encoded protein function: FUNCTION: Activation of pyruvate formate-lyase 1 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. EcoCyc product frame: PFLACTENZ-MONOMER. EcoCyc synonyms: act. Genomic coordinates: 950340-951080. EcoCyc protein note: Under anaerobic conditions, pyruvate formate-lyase activating enzyme (PflA, PFL-AE) activates PYRUVFORMLY-MONOMER by generating an essential glycyl radical within the enzyme . PFL-AE belongs to the radical SAM superfamily of proteins . The enzyme is also capable of activating the tdcE-encoded KETOBUTFORMLY-INACT-MONOMER and EG11784-MONOMER . PFL-AE uses S-adenosylmethionine (SAM) and reduced flavodoxin as co-substrates to produce the glycyl radical, generating 5'-deoxyadenosine and methionine as side products. The pro-S hydrogen from Gly734 in pyruvate formate-lyase is abstracted by the 5'-deoxyadenosyl radical in the active site of PFL-AE and incorporated into 5'-deoxyadenosine . The interaction of the enzyme with SAM and the mechanism of radical generation has been investigated . Formation of an organometallic intermediate, Ω, which consists of an Fe-C5' bond between the 5'-deoxyadenosyl radical and the [4Fe4S] cluster, is central to catalysis...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9N4|protein.P0A9N4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pflA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003068,ECOCYC:EG10028,GeneID:945517`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:950340-951080:-; feature_type=gene
