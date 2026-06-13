---
entity_id: "protein.P76135"
entity_type: "protein"
name: "ydeO"
source_database: "UniProt"
source_id: "P76135"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydeO b1499 JW1494"
---

# ydeO

`protein.P76135`

## Static

- Type: `protein`
- Source: `UniProt:P76135`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Induces the expression of gadE and mdtEF. Could also regulate the expression of other genes involved in acid resistance. {ECO:0000269|PubMed:12694615}. YdeO belongs to the AraC/XylS family of transcriptional regulators and shows more similarity to YhiW, AppY, AdiY, and GadX than the other AraC/XylS regulators . The members of this family exhibit two domains, an amino-terminal domain involved in coinducer recognition and dimerization and a carboxy-terminal domain that contains a potential helix-turn-helix DNA-binding motif . YdeO activates genes involved in the cellular response to acid resistance . This protein, together with the proteins HNS, EvgA, and GadE, pertains to a specific regulatory circuit that is functional in exponential-phase cells growing in minimal medium . Several of the genes directly regulated by YdeO are also directly regulated by GadX . The YdeO regulon has been determined . Based on ChIP-chip, RT-qPCR, EMSA, DNase I footprinting, and reporter assay, 7 new operons were identified as members of the YdeO regulon, including four stress response transcription factors, DctR, NhaR, GadE, and Gad, and several genes involved in respiration . YdeO plays an important role in survival under both acidic and anaerobic conditions , and also appears to have a role in biofilm formation, mainly in E...

## Annotation

FUNCTION: Induces the expression of gadE and mdtEF. Could also regulate the expression of other genes involved in acid resistance. {ECO:0000269|PubMed:12694615}.

## Outgoing Edges (22)

- `activates` --> [[gene.b0020|gene.b0020]] `RegulonDB` `S` - regulator=YdeO; target=nhaR; function=+
- `activates` --> [[gene.b0972|gene.b0972]] `RegulonDB` `S` - regulator=YdeO; target=hyaA; function=+
- `activates` --> [[gene.b0973|gene.b0973]] `RegulonDB` `S` - regulator=YdeO; target=hyaB; function=+
- `activates` --> [[gene.b0974|gene.b0974]] `RegulonDB` `S` - regulator=YdeO; target=hyaC; function=+
- `activates` --> [[gene.b0975|gene.b0975]] `RegulonDB` `S` - regulator=YdeO; target=hyaD; function=+
- `activates` --> [[gene.b0976|gene.b0976]] `RegulonDB` `S` - regulator=YdeO; target=hyaE; function=+
- `activates` --> [[gene.b0977|gene.b0977]] `RegulonDB` `S` - regulator=YdeO; target=hyaF; function=+
- `activates` --> [[gene.b0978|gene.b0978]] `RegulonDB` `S` - regulator=YdeO; target=appC; function=+
- `activates` --> [[gene.b0979|gene.b0979]] `RegulonDB` `S` - regulator=YdeO; target=appB; function=+
- `activates` --> [[gene.b0980|gene.b0980]] `RegulonDB` `S` - regulator=YdeO; target=appA; function=+
- `activates` --> [[gene.b1493|gene.b1493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3506|gene.b3506]] `RegulonDB` `S` - regulator=YdeO; target=slp; function=+
- `activates` --> [[gene.b3507|gene.b3507]] `RegulonDB` `S` - regulator=YdeO; target=dctR; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=YdeO; target=gadE; function=+
- `activates` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - regulator=YdeO; target=mdtE; function=+
- `activates` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - regulator=YdeO; target=mdtF; function=+
- `activates` --> [[gene.b3515|gene.b3515]] `RegulonDB` `S` - regulator=YdeO; target=gadW; function=+
- `activates` --> [[gene.b3922|gene.b3922]] `RegulonDB` `S` - regulator=YdeO; target=yiiS; function=+
- `activates` --> [[gene.b3923|gene.b3923]] `RegulonDB` `S` - regulator=YdeO; target=uspD; function=+
- `activates` --> [[gene.b4592|gene.b4592]] `RegulonDB` `S` - regulator=YdeO; target=appX; function=+
- `activates` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - regulator=YdeO; target=gadF; function=+
- `represses` --> [[gene.b4117|gene.b4117]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1499|gene.b1499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76135`
- `KEGG:ecj:JW1494;eco:b1499;ecoc:C3026_08680;`
- `GeneID:945922;`
- `GO:GO:0000976; GO:0003700; GO:0006351; GO:0006355; GO:0045893`

## Notes

HTH-type transcriptional regulator YdeO
