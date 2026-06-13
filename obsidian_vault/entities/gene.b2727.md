---
entity_id: "gene.b2727"
entity_type: "gene"
name: "hypB"
source_database: "NCBI RefSeq"
source_id: "gene-b2727"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2727"
  - "hypB"
---

# hypB

`gene.b2727`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2727`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hypB (gene.b2727) is a gene entity. It encodes hypB (protein.P0AAN3). Encoded protein function: FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:7601092, PubMed:8756471). Exhibits a low intrinsic GTPase activity, which is essential for nickel insertion (PubMed:21544686, PubMed:27951644, PubMed:7601092). In the presence of GDP, nickel, but not zinc, is transferred from the HypB GTPase domain (G-domain) to HypA (PubMed:23899293, PubMed:27951644). {ECO:0000269|PubMed:21544686, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644, ECO:0000269|PubMed:7601092, ECO:0000269|PubMed:8756471}. EcoCyc product frame: EG10484-MONOMER. EcoCyc synonyms: hydB. Genomic coordinates: 2851001-2851873. EcoCyc protein note: The HypB protein is an accessory protein involved in the maturation of all hydrogenase isoenzymes. It is required for the incorporation of nickel into the large subunit of hydrogenases in vivo and in vitro . HypB binds Ni2+ with sub-picomolar KD in approximately stoichiometric amounts; the binding site was localized to the N-terminal CXXCGC motif and characterized extensively . A short peptide containing this motif retains Ni2+ binding activity . A low-affinity metal binding site with preference for Zn2+ exists in the C-terminal GTPase domain . Both sites are required for HypB activity...

## Biological Role

Activated by fnr (protein.P0A9E5), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAN3|protein.P0AAN3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=hypB; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hypB; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hypB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008960,ECOCYC:EG10484,GeneID:947194`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2851001-2851873:+; feature_type=gene
