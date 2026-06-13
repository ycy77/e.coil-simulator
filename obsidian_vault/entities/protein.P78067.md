---
entity_id: "protein.P78067"
entity_type: "protein"
name: "ynjE"
source_database: "UniProt"
source_id: "P78067"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynjE b1757 JW5287"
---

# ynjE

`protein.P78067`

## Static

- Type: `protein`
- Source: `UniProt:P78067`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

Thiosulfate sulfurtransferase YnjE (EC 2.8.1.1) YnjE is a monomeric sulfurtransferase containing three rhodanese-like domains. In vitro, the sulfurtransferase G7325 IscS is able to transfer sulfur to the active site cysteine of YnjE; both thiosulfate and 3-mercaptopyruvate are poor sulfate donors. The physiological substrate of YnjE was unknown for a while . However, a later study showed a potential role of the enzyme in molybdopterin biosynthesis . Similarly to the eukaryotic rhodanese MOCS3, YnjE was shown to enhance the rate of PRECURSOR-Z conversion to CPD-4 in vitro, yet it was not an enhancer of the cysteine desulfurase activity of G7325 IscS. The protein was also shown to interact with EG10154 MoeB in vivo under anaerobic conditions, supporting a role in transferring a sulfur from IscS to the Carboxyadenylated-MPT-synthases "carboxy-adenylated MoaD", forming the thiocarboxylated form that is required for the CPLX0-2502 activity . Crystal structures of YnjE in its sulfur-free and persulfurated state (2.4 Å resolution) have been solved. The active site is located in a cleft at the interface between the central and C-terminal rhodanese domains. Site-directed mutagenesis of the active site loop showed that it is not the only determinant for substrate specificity . Transcription of ynjE is increased under anaerobic conditions .

## Biological Role

Catalyzes RXN-12473 (reaction.ecocyc.RXN-12473).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

Thiosulfate sulfurtransferase YnjE (EC 2.8.1.1)

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12473|reaction.ecocyc.RXN-12473]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1757|gene.b1757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P78067`
- `KEGG:ecj:JW5287;eco:b1757;ecoc:C3026_10030;`
- `GeneID:946505;`
- `GO:GO:0004792; GO:0016783; GO:0042597`
- `EC:2.8.1.1`

## Notes

Thiosulfate sulfurtransferase YnjE (EC 2.8.1.1)
