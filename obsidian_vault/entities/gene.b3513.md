---
entity_id: "gene.b3513"
entity_type: "gene"
name: "mdtE"
source_database: "NCBI RefSeq"
source_id: "gene-b3513"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3513"
  - "mdtE"
---

# mdtE

`gene.b3513`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3513`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtE (gene.b3513) is a gene entity. It encodes mdtE (protein.P37636). Encoded protein function: FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}. EcoCyc product frame: EG12240-MONOMER. EcoCyc synonyms: yhiU. Genomic coordinates: 3659232-3660389. EcoCyc protein note: MdtE is the membrane fusion protein of a putative tripartite efflux pump complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12 (see TRANS-CPLX-204 for more detail). Production of MdtE does not complement the efflux defect of E. coli strain HNCE3 (nonpolar ΔacrA) (. MdtE is a member of the Membrane Fusion Protein (MFP) family . MdtE was isolated as a homotrimer in inner membrane vesicles purified from E. coli strain BL21 . Exposure to synthetic reactive oxygen species (ROS) generated from synthetron radiation (X-ray) results in oxidation of methionine residues in vivo in hundreds of proteins. The % modification was highest in MdtE, EG11009-MONOMER TolC and EG10855-MONOMER and increased as the X-ray oxidation dose increased .

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8), fliZ (protein.P52627), nac (protein.Q47005). Activated by rpoD (protein.P00579), evgA (protein.P0ACZ4), rpoS (protein.P13445), gadX (protein.P37639), gadE (protein.P63204), ydeO (protein.P76135), nac (protein.Q47005), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37636|protein.P37636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (12)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdtE; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=mdtE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mdtE; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=mdtE; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=mdtE; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=mdtE; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mdtE; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=mdtE; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mdtE; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `C` - regulator=FliZ; target=mdtE; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mdtE; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011478,ECOCYC:EG12240,GeneID:948031`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3659232-3660389:+; feature_type=gene
