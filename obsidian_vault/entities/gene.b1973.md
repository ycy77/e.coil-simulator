---
entity_id: "gene.b1973"
entity_type: "gene"
name: "zinT"
source_database: "NCBI RefSeq"
source_id: "gene-b1973"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1973"
  - "zinT"
---

# zinT

`gene.b1973`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1973`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zinT (gene.b1973) is a gene entity. It encodes zinT (protein.P76344). Encoded protein function: FUNCTION: May function as a periplasmic zinc chaperone or mediate direct transport of zinc from the periplasm to the cytoplasm under zinc-limited conditions. Binds zinc with high affinity, and can also bind cadmium, mercury or nickel. Preferentially binds Zn(2+) over Cd(2+). Contains one high affinity metal binding site, and can bind additional metal ions at other sites. {ECO:0000269|PubMed:17931600, ECO:0000269|PubMed:19377097}. EcoCyc product frame: G7061-MONOMER. EcoCyc synonyms: yodA. Genomic coordinates: 2041375-2042025. EcoCyc protein note: Best characterised in TAX-90371, the periplasmic metal-binding protein ZinT functions as an accessory component of the ABC-63-CPLX ZnuABC transporter by delivering Zn2+ to ZnuA under conditions of severe Zn2+ shortage . ZinT contributes to ZnuA-mediated recruitment of zinc in the periplasmic space in TAX-83334 . ZinT consists of a major lipocalin-like domain and a smaller helical domain; purified ZinT binds metals such as cadmium and zinc and crystal structures have been determined . Purified ZinT binds zinc, cadmium, mercury and possibly nickel . Purified ZinT preferentially binds Zn2+ over Cd2+...

## Biological Role

Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76344|protein.P76344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=zinT; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=zinT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006546,ECOCYC:G7061,GeneID:946480`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2041375-2042025:+; feature_type=gene
