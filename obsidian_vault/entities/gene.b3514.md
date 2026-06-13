---
entity_id: "gene.b3514"
entity_type: "gene"
name: "mdtF"
source_database: "NCBI RefSeq"
source_id: "gene-b3514"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3514"
  - "mdtF"
---

# mdtF

`gene.b3514`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3514`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtF (gene.b3514) is a gene entity. It encodes mdtF (protein.P37637). Encoded protein function: FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}. EcoCyc product frame: YHIV-MONOMER. EcoCyc synonyms: yhiV. Genomic coordinates: 3660414-3663527. EcoCyc protein note: MdtF is the inner membrane subunit of a putative tripartite efflux complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12 (see TRANS-CPLX-204 for more detail). MdtF can function with the AcrA membrane fusion protein for efflux of bile salts (cholate, taurocholate), dyes (crystal violet, ethidium bromide) and antibiotics (novobiocin, ciprofloxacin, eerythromycin) . mdtF expressed from a plasmid can complement the steroid hormone efflux deficient phenotype of a strain lacking both AcrB and EmrAB MdtF was isolated as a homotrimer in inner membrane vesicles purified from E. coli strain BL21 MdtF belongs to the Hydrophobe/Amphiphile Efflux-1 (HAE1) family of transporters within the resistance-nodulation-cell division (RND) superfamily...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8), yeiE (protein.P0ACR4), fliZ (protein.P52627), nac (protein.Q47005). Activated by rpoD (protein.P00579), evgA (protein.P0ACZ4), rpoS (protein.P13445), gadX (protein.P37639), gadE (protein.P63204), ydeO (protein.P76135), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37637|protein.P37637]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (12)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdtF; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=mdtF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mdtF; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=mdtF; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=mdtF; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=mdtF; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=mdtF; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mdtF; function=-
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `C` - regulator=FliZ; target=mdtF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mdtF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011480,ECOCYC:EG12241,GeneID:948030`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3660414-3663527:+; feature_type=gene
